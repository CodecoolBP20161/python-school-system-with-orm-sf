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
    {'first_name': 'Kata', 'last_name': 'Kiss', 'city': 'Budapest', 'status': 'applied', 'email': 'kata.ki@gmail.com'},
    {'first_name': 'Zoltán', 'last_name': 'Nagy', 'city': 'Debrecen','status': 'applied', 'email': 'zolika@gmail.com'},
    {'first_name': 'László', 'last_name': 'Közepes', 'city': 'Eger','status': 'applied', 'email': 'laci.ko@gmail.com'},
    {'first_name': 'Ryan', 'last_name': 'Gostling', 'city': 'Los Angeles','status': 'applied','email':'r@gmail.com'},
    {'first_name': 'Lilla', 'last_name': 'Lila', 'city': 'Székesfehérvár','status': 'applied', 'email':'l@hotmail.com'},
    {'first_name': 'Alina', 'last_name': 'Kolowa', 'city': 'Krakkó','status': 'applied', 'email': 'alina@hotmail.com'},
    {'first_name': 'Tibor', 'last_name': 'Valami', 'city': 'Dabas','status': 'applied', 'email': 'tibi@freemail.com'},
    {'first_name': 'Max', 'last_name': 'Well', 'city': 'New York','status': 'applied', 'email': 'maxy@gmail.com'},
    {'first_name': 'Marek', 'last_name': 'Saro', 'city': 'Varsó','status': 'applied', 'email':'saro@gmail.com'},
    {'first_name': 'Miklós', 'last_name': 'Siklós', 'city': 'Miskolc','status': 'applied', 'email': 'mi@gmail.com'}
]


def add_applicants():
    for applicant in applicants:
        Applicant.create(first_name=applicant['first_name'], last_name=applicant['last_name'], city=applicant['city'],
                         status=applicant['status'], email=applicant['email'])



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
    {'start': '2016-09-01 11:00:00', 'end': '2016-09-01 11:20:00', 'free': True},
    {'start': '2016-09-01 11:30:00', 'end': '2016-09-01 11:50:00', 'free': True},
    {'start': '2016-09-01 13:00:00', 'end': '2016-09-01 13:20:00', 'free': True},
    {'start': '2016-09-01 13:30:00', 'end': '2016-09-01 13:50:00', 'free': True},
    {'start': '2016-09-02 11:00:00', 'end': '2016-09-02 11:20:00', 'free': True},
    {'start': '2016-09-02 11:30:00', 'end': '2016-09-02 11:50:00', 'free': True},
    {'start': '2016-09-02 13:00:00', 'end': '2016-09-02 13:20:00', 'free': True},
    {'start': '2016-09-02 11:00:00', 'end': '2016-09-02 11:20:00', 'free': True},
    {'start': '2016-09-03 11:00:00', 'end': '2016-09-03 11:20:00', 'free': True},
    {'start': '2016-09-03 11:30:00', 'end': '2016-09-03 11:50:00', 'free': True},
    {'start': '2016-09-04 11:00:00', 'end': '2016-09-04 11:20:00', 'free': True},
    {'start': '2016-09-04 11:00:00', 'end': '2016-09-04 11:20:00', 'free': True},
    {'start': '2016-09-04 11:40:00', 'end': '2016-09-04 12:00:00', 'free': True},
    {'start': '2016-09-05 13:00:00', 'end': '2016-09-05 13:20:00', 'free': True},
    {'start': '2016-09-05 13:30:00', 'end': '2016-09-05 13:50:00', 'free': True},
    {'start': '2016-09-06 11:00:00', 'end': '2016-09-06 11:20:00', 'free': True}
]


def interview():
    for interview_slot in interview_slots:
        Interview.create(start=interview_slot['start'], end=interview_slot['end'],free=interview_slot['free'])


assign_mentors = [{'interview': '1', 'mentor': '1'},
                  {'interview': '1', 'mentor': '3'},
                  {'interview': '2', 'mentor': '2'},
                  {'interview': '2', 'mentor': '3'},
                  {'interview': '3', 'mentor': '1'},
                  {'interview': '3', 'mentor': '2'}]


def assign_mentors():
    for mentors in assign_mentors:
        Assign_mentors.create(interview = Interview.select().where(Interview.id == mentors['interview']),
                              mentor = Mentor.select().where(Mentor.id == mentors['mentor']))

