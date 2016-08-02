from peewee import *
from connect import db


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


class Interview(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    mentor = ForeignKeyField(Mentor, related_name='interviews')
    free = BooleanField(default=True)

    def __str__(self):
        return str(self.id)


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
            applicant.set_interview_slot()

    def set_interview_slot(self):
        query = (Interview.select(Interview, Mentor)
                 .join(Mentor)
                 .where(Interview.free, Mentor.school == self.school))
        try:
            slot = [i for i in query][0]
            slot.free = False
            slot.save()
            self.interview_slot = slot
            self.save()
        except IndexError:
            print('Not enough interview slots!')


class City(BaseModel):
    name = CharField()
    school_near = ForeignKeyField(School, related_name='schools')


class Question(BaseModel):
    status = CharField()
    time = DateTimeField()
    applicant = ForeignKeyField(Applicant, related_name='applicant_name')
    question = TextField()
    mentor = ForeignKeyField(Mentor, related_name='mentor_name')
