from peewee import *


def connect_to_db():
    import getpass
    db_name = input('DB name: ')
    db_user = input('DB user: ')
    db_password = getpass.getpass('DB user password: ')
    return PostgresqlDatabase(db_name, user=db_user, password=db_password)

db = connect_to_db()


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


class City(BaseModel):
    name = CharField()
    school_near = ForeignKeyField(School, related_name='schools')
