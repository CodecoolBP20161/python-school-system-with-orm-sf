from peewee import *
from connect import db

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()


class Applicant(BaseModel):
    application_code = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School, related_name='applicants', null=True)

    @classmethod
    def find_missing_app_code(cls):
        return Applicant.select().where(Applicant.application_code >> None)

    @classmethod
    def find_missing_school(cls):
        return Applicant.select().where(Applicant.school >> None)

    @classmethod
    def finding_city(cls):
        applicants = cls.find_missing_app_school()
        for applicant in applicants:
            applicant.set_city()

    def set_city(self):
        self.school = City.select(City.school_near).where(City.name == self.city)
        self.save()

    @classmethod
    def set_app_code(cls):
        from code_gener import pw
        pw()


class City(BaseModel):
    name = CharField()
    school_near = ForeignKeyField(School, related_name='schools')

