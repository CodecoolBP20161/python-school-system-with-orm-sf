from models import *


class ApplicantLogin():

    appcode = None

    @classmethod
    def login(cls):
        passwd = input("Please add an application code: ")
        if Applicant.select().where(Applicant.application_code == passwd):
            cls.appcode = passwd
            return True
        else:
            print("No such applicant")
            return False

    @classmethod
    def status(cls):
        """Application details"""
        return Applicant.select(Applicant.status, School.location.alias('School')).join(School)\
                        .where(Applicant.application_code == cls.appcode)

    @classmethod
    def by_date_school_mentor(cls):
        return Applicant.select(Interview.start, School.location, AssignMentor.mentor_id) \
            .join(AssignMentor).join(Interview).switch(Applicant).join(School) \
            .where(Applicant.application_code == cls.appcode)
