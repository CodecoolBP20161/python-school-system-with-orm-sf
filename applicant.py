from models import *

class ApplicantLogin():

    def __init__(self,  appcode):
        self.appcode = appcode

    @classmethod
    def login(cls):
        passwd = input("Please add a passcode")
        if Applicant.get(application_code == passwd):
            return ApplicantLogin(appcode)
        else:
            print("No such applicant")

    def status(self):
        return Applicant.select(Applicant.status).where(Applicant.application_code == self.appcode)
