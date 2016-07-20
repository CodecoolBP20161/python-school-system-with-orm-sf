from peewee import *
from connect import db





class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()


class Applicant(BaseModel):
    application_code = CharField(default='None')
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School,null = True, related_name='applicants')

    @classmethod
    def find_missing_app_code():
        return Applicant.select().where(Applicant.application_code >> None)


class City(BaseModel):
    name = CharField()
    school_near = ForeignKeyField(School, related_name='schools')
