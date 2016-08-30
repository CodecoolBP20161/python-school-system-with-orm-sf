from peewee import *
from connect import db
from mail import Mail

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()

    def __str__(self):
        return self.location


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='mentors')
    email = CharField()

    def _send_interview_details(self, slot, applicant):
        message = "Dear %s!\n\nYour You have an interview at: %s\nApplicant's name: %s\n\nHave fun!" \
                  % (self.first_name + ' ' + self.last_name, slot.start, applicant.first_name + ' ' + applicant.last_name)
        Mail.send(message, self.email, 'Interview details')


class Interview(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    free = BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class AssignMentor(BaseModel):
    interview = ForeignKeyField(Interview, related_name='mentors', null=True)
    mentor = ForeignKeyField(Mentor, related_name='interviews', null=True)


class Applicant(BaseModel):
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School, related_name='applicants', null=True)
    interview_slot = ForeignKeyField(Interview, related_name='applicants', null=True)
    status = CharField()
    email = CharField()

    @classmethod
    def find_missing_app_code(cls):
        return Applicant.select().where(Applicant.application_code >> None)

    @classmethod
    def find_missing_school(cls):
        return Applicant.select().where(Applicant.school >> None)

    @classmethod
    def finding_city(cls):
        """Find closest school for applicants"""
        applicants = cls.find_missing_school()
        for applicant in applicants:
            applicant.set_city()

    def set_city(self):
        self.school = City.select(City.school_near).where(City.name == self.city)
        self.save()
        self._send_app_code_school()


    @classmethod
    def set_app_code(cls):
        """Set application code for applicants"""
        from code_gener import pw
        pw()

    @classmethod
    def find_missing_interview_slot(cls):
        return Applicant.select().where(Applicant.interview_slot >> None)

    @classmethod
    def assign_interview_slot(cls):
        """Find interview slot for applicant"""
        applicants = cls.find_missing_interview_slot()
        for applicant in applicants:
            applicant.assign_slot_with_mentors()

    def assign_slot_with_mentors(self):
        print(self.first_name)
        query = Interview.select().where(Interview.free)
        have_slot = True
        j = 0
        slots = [i for i in query]
        while have_slot:
            try:
                slot = slots[j]
            except IndexError:
                print('Not enough interview slot')
                have_slot = False
                continue
            query = (AssignMentor.select(Mentor.id)
                     .join(Mentor).switch(AssignMentor).join(Interview)
                     .where(slot.start == Interview.start))
            query2 = Mentor.select().where(Mentor.id.not_in(query), Mentor.school == self.school)
            try:
                enough_mentor = [i for i in query2][1]
            except IndexError:
                j += 1
                continue
            for m in range(2):
                AssignMentor.create(interview=slot, mentor=[i for i in query2][m])
            slot.free = False
            slot.save()
            self.interview_slot = slot
            self.save()
            self._send_interview_slot_email(query2)
            for mentor in query2[:2]:
                mentor._send_interview_details(slot, applicant=self)
            have_slot = False

    def _send_interview_slot_email(self, mentors):
        message = "Dear %s!\n\nYour interview's time: %s\nAssigned mentors: %s, %s\n\n See you soon!" \
                  % (self.first_name + ' ' + self.last_name, self.interview_slot.start,
                     mentors[0].first_name + ' ' + mentors[0].last_name,
                     mentors[1].first_name + ' ' + mentors[1].last_name)
        Mail.send(message, self.email, 'Interview time')

    def _send_app_code_school(self):
        message = "Dear %s!\n\nYour Application code: %s\nAssigned school: %s\n\nFarewell" \
                  % (self.first_name + ' ' + self.last_name, self.application_code, self.school.location)
        Mail.send(message, self.email, 'Application details')





class City(BaseModel):
    name = CharField()
    school_near = ForeignKeyField(School, related_name='schools')


class Question(BaseModel):
    status = CharField()
    time = DateTimeField()
    applicant = ForeignKeyField(Applicant, related_name='questions', null=True)
    question = TextField()
    mentor = ForeignKeyField(Mentor, related_name='questions', null=True)


class EmailLog(BaseModel):
    subject = CharField()
    content = TextField()
    mode = CharField()
    timestamp = DateTimeField()
    recipient_name = CharField()
    recipient_email = CharField()
    status = BooleanField()
