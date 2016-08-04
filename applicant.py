from models import *


class ApplicantLogin():
    def __init__(self, appcode):
        self.appcode = appcode

    @classmethod
    def login(cls):
        passwd = input("Please add a passcode")
        if Applicant.get(application_code == passwd):
            return ApplicantLogin(appcode)
        else:
            print("No such applicant")


    @classmethod
    def by_date_school_mentor(cls):
        return Applicant.select(Interview.start, School.location, Assignmentor.mentor_id) \
            .join(Assignmentor).join(Interview).switch(Applicant).join(School) \
            .where(Applicant.application_code == cls.appcode)
