from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('cave', user='cave', password='123456789')


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
    school = ForeignKeyField(School, default='None', related_name='applicants')


class City(BaseModel):
    name = CharField()
    school_near = ForeignKeyField(School, related_name='schools')

