# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

schools = [
    {'location': 'Budapest'},
    {'location': 'Miskolc'},
    {'location': 'Krakkó'},
    {'location': 'Los Angeles'}

]


def add_schools():
    for school in schools:
        School.create(location=school['location'])

applicants = [
    {'first_name': 'Kata', 'last_name': 'Kiss', 'city': 'Budapest'},
    {'first_name': 'Zoltán', 'last_name': 'Nagy', 'city': 'Debrecen'},
    {'first_name': 'László', 'last_name': 'Közepes', 'city': 'Eger'},
    {'first_name': 'Ryan', 'last_name': 'Gostling', 'city': 'Los Angeles'},
    {'first_name': 'Lilla', 'last_name': 'Lila', 'city': 'Székesfehérvár'},
    {'first_name': 'Alina', 'last_name': 'Kolowa', 'city': 'Krakkó'},
    {'first_name': 'Tibor', 'last_name': 'Valami', 'city': 'Dabas'},
    {'first_name': 'Max', 'last_name': 'Well', 'city': 'New York'},
    {'first_name': 'Marek', 'last_name': 'Saro', 'city': 'Varsó'},
    {'first_name': 'Miklós', 'last_name': 'Siklós', 'city': 'Miskolc'}
]


def add_applicants():
    for applicant in applicants:
        Applicant.create(first_name=applicant['first_name'], last_name=applicant['last_name'], city=applicant['city'])


cities = [
    {'name': 'Budapest', 'school_near': 'Budapest'},
    {'name': 'Debrecen', 'school_near': 'Miskolc'},
    {'name': 'Eger', 'school_near': 'Miskolc'},
    {'name': 'Los Angeles', 'school_near': 'Los Angeles'},
    {'name': 'Székesfehérvár', 'school_near': 'Budapest'},
    {'name': 'Krakkó', 'school_near': 'Krakkó'},
    {'name': 'Dabas', 'school_near': 'Budapest'},
    {'name': 'New York', 'school_near': 'Los Angeles'},
    {'name': 'Varsó', 'school_near': 'Krakkó'},
    {'name': 'Miskolc', 'school_near': 'Miskolc'}
]


def add_cities():
    for city in cities:
        City.create(name=city['name'], school_near=School.select().where(School.location == city['school_near']))


mentors = [
    {'first_name': 'Miki', 'last_name': 'Beöthy', 'school': 'Budapest'},
    {'first_name': 'Tomi', 'last_name': 'Tompa', 'school': 'Budapest'},
    {'first_name': 'Dani', 'last_name': 'Salamon', 'school': 'Budapest'},
    {'first_name': 'Zoli', 'last_name': 'Ász', 'school': 'Miskolc'},
    {'first_name': 'Hrosic', 'last_name': 'Czukor', 'school': 'Krakkó'}
]


def add_mentors():
    for mentor in mentors:
        Mentor.create(first_name=mentor['first_name'], last_name=mentor['last_name'],
                      school=School.select().where(School.location == mentor['school']))

interview_slots = [
    {'start': '2016-09-01 11:00:00', 'end': '2016-09-01 11:20:00', 'mentor': 'Miki', 'free': True},
    {'start': '2016-09-01 11:30:00', 'end': '2016-09-01 11:50:00', 'mentor': 'Miki', 'free': True},
    {'start': '2016-09-01 13:00:00', 'end': '2016-09-01 13:20:00', 'mentor': 'Tomi', 'free': False},
    {'start': '2016-09-01 13:30:00', 'end': '2016-09-01 13:50:00', 'mentor': 'Miki', 'free': True},
    {'start': '2016-09-02 11:00:00', 'end': '2016-09-01 11:20:00', 'mentor': 'Zoli', 'free': True},
    {'start': '2016-09-02 11:30:00', 'end': '2016-09-01 11:50:00', 'mentor': 'Zoli', 'free': True},
    {'start': '2016-09-02 13:00:00', 'end': '2016-09-01 13:20:00', 'mentor': 'Zoli', 'free': False},
    {'start': '2016-09-02 11:00:00', 'end': '2016-09-01 11:20:00', 'mentor': 'Miki', 'free': True},
    {'start': '2016-09-03 11:00:00', 'end': '2016-09-01 11:20:00', 'mentor': 'Hrosic', 'free': True},
    {'start': '2016-09-03 11:30:00', 'end': '2016-09-01 11:50:00', 'mentor': 'Hrosic', 'free': False},
    {'start': '2016-09-04 11:00:00', 'end': '2016-09-01 11:20:00', 'mentor': 'Hrosic', 'free': True},
    {'start': '2016-09-04 11:00:00', 'end': '2016-09-01 11:20:00', 'mentor': 'Miki', 'free': True},
]


def interview():
    for interview_slot in interview_slots:
        Interview.create(start=interview_slot['start'], end=interview_slot['end'],
                         mentor=Mentor.select().where(Mentor.first_name == interview_slot['mentor']),
                         free=interview_slot['free'])
