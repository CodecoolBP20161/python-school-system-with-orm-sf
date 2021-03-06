# This script can generate example data for "City" and "InterviewSlot" models.

from models import *
import random

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
    {'first_name': 'Kata', 'last_name': 'Kiss', 'city': 'Budapest', 'status': 'applied', 'email': 'applicant.codecool@gmail.com'},
    {'first_name': 'Zoltán', 'last_name': 'Nagy', 'city': 'Debrecen','status': 'applied', 'email': 'applicant.codecool+a1@gmail.com'},
    {'first_name': 'László', 'last_name': 'Közepes', 'city': 'Eger','status': 'applied', 'email': 'applicant.codecool+a2@gmail.com'},
    {'first_name': 'Ryan', 'last_name': 'Gostling', 'city': 'Los Angeles','status': 'applied','email':'applicant.codecool+a3@gmail.com'},
    {'first_name': 'Lilla', 'last_name': 'Lila', 'city': 'Székesfehérvár','status': 'applied', 'email':'applicant.codecool+a4@gmail.com'},
    {'first_name': 'Alina', 'last_name': 'Kolowa', 'city': 'Krakkó','status': 'applied', 'email': 'applicant.codecool+a5@gmail.com'},
    {'first_name': 'Tibor', 'last_name': 'Valami', 'city': 'Dabas','status': 'applied', 'email': 'applicant.codecool+a6@gmail.com'},
    {'first_name': 'Max', 'last_name': 'Well', 'city': 'New York','status': 'applied', 'email': 'applicant.codecool+a7@gmail.com'},
    {'first_name': 'Marek', 'last_name': 'Saro', 'city': 'Varsó','status': 'applied', 'email':'applicant.codecool+a8@gmail.com'},
    {'first_name': 'Miklós', 'last_name': 'Siklós', 'city': 'Miskolc','status': 'applied', 'email': 'applicant.codecool+a9@gmail.com'}
]


def add_applicants():
    for applicant in applicants:
        Applicant.create(first_name=applicant['first_name'], last_name=applicant['last_name'], city=applicant['city'],
                         status=applicant['status'], email=applicant['email'])


mentors = [
    {'first_name': 'Miki', 'last_name': 'Beöthy', 'school': 'Budapest','email':'applicant.codecool+m@gmail.com'},
    {'first_name': 'Tomi', 'last_name': 'Tompa', 'school': 'Budapest','email':'applicant.codecool+m1@gmail.com'},
    {'first_name': 'Dani', 'last_name': 'Salamon', 'school': 'Budapest','email':'applicant.codecool+m2@gmail.com'},
    {'first_name': 'Zoli', 'last_name': 'Ász', 'school': 'Miskolc','email':'applicant.codecool+m3@gmail.com'},
    {'first_name': 'Pista', 'last_name': 'Kovács', 'school': 'Miskolc','email':'applicant.codecool+m4@gmail.com'},
    {'first_name': 'Imre', 'last_name': 'Szabó', 'school': 'Miskolc','email':'applicant.codecool+m5@gmail.com'},
    {'first_name': 'Hrosic', 'last_name': 'Czukor', 'school': 'Krakkó','email':'applicant.codecool+m6@gmail.com'},
    {'first_name': 'Béla', 'last_name': 'Lengyel', 'school': 'Krakkó','email':'applicant.codecool+m7@gmail.com'},
    {'first_name': 'Réka', 'last_name': 'Sárga', 'school': 'Krakkó','email':'applicant.codecool+m8@gmail.com'}

]


def add_mentors():
    for mentor in mentors:
        Mentor.create(first_name=mentor['first_name'], last_name=mentor['last_name'],email=mentor['email'],
                      school=School.select().where(School.location == mentor['school']))

interview_slots = [
    {'start': '2016-09-01 11:00:00', 'end': '2016-09-01 11:20:00', 'free': True},
    {'start': '2016-09-01 11:00:00', 'end': '2016-09-01 11:20:00', 'free': True},
    {'start': '2016-09-01 11:00:00', 'end': '2016-09-01 11:20:00', 'free': True},
    {'start': '2016-09-01 11:30:00', 'end': '2016-09-01 11:50:00', 'free': True},
    {'start': '2016-09-01 11:30:00', 'end': '2016-09-01 11:50:00', 'free': True},
    {'start': '2016-09-01 13:00:00', 'end': '2016-09-01 13:20:00', 'free': True},
    {'start': '2016-09-01 13:00:00', 'end': '2016-09-01 13:20:00', 'free': True},
    {'start': '2016-09-01 13:30:00', 'end': '2016-09-01 13:50:00', 'free': True},
    {'start': '2016-09-02 11:00:00', 'end': '2016-09-02 11:20:00', 'free': True},
    {'start': '2016-09-02 11:30:00', 'end': '2016-09-02 11:50:00', 'free': True},
    {'start': '2016-09-02 13:00:00', 'end': '2016-09-02 13:20:00', 'free': True},
    {'start': '2016-09-02 11:00:00', 'end': '2016-09-02 11:20:00', 'free': True},
    {'start': '2016-09-03 11:00:00', 'end': '2016-09-03 11:20:00', 'free': True},
    {'start': '2016-09-03 11:30:00', 'end': '2016-09-03 11:50:00', 'free': True},
    {'start': '2016-09-03 11:30:00', 'end': '2016-09-03 11:50:00', 'free': True},
    {'start': '2016-09-03 11:30:00', 'end': '2016-09-03 11:50:00', 'free': True},
    {'start': '2016-09-03 11:30:00', 'end': '2016-09-03 11:50:00', 'free': True},
    {'start': '2016-09-04 11:00:00', 'end': '2016-09-04 11:20:00', 'free': True},
    {'start': '2016-09-04 11:00:00', 'end': '2016-09-04 11:20:00', 'free': True},
    {'start': '2016-09-04 11:40:00', 'end': '2016-09-04 12:00:00', 'free': True},
    {'start': '2016-09-04 11:40:00', 'end': '2016-09-04 12:00:00', 'free': True},
    {'start': '2016-09-04 11:40:00', 'end': '2016-09-04 12:00:00', 'free': True},
    {'start': '2016-09-04 11:40:00', 'end': '2016-09-04 12:00:00', 'free': True},
    {'start': '2016-09-05 13:00:00', 'end': '2016-09-05 13:20:00', 'free': True},
    {'start': '2016-09-05 13:30:00', 'end': '2016-09-05 13:50:00', 'free': True},
    {'start': '2016-09-06 11:00:00', 'end': '2016-09-06 11:20:00', 'free': True}
]


def interview():
    for interview_slot in interview_slots:
        Interview.create(start=interview_slot['start'], end=interview_slot['end'], free=interview_slot['free'])


questions = [
    {'question': 'Why I have to speak English?', 'status': 'new', 'time': '2016-09-01 11:20:00'},
    {'question': 'How much time activity is needed?', 'status': 'new', 'time': '2016-09-02 10:20:00'},
    {'question': 'Are there any break during the education?', 'status': 'new', 'time': '2016-09-03 20:20:00'},
    {'question': 'What kind of company can I work at?', 'status': 'new', 'time': '2016-09-03 21:21:00'},
    {'question': 'How much will be the starting wage?', 'status': 'new', 'time': '2016-09-04 22:21:00'},
    {'question': 'How much money I have to pay back after finishing?', 'status': 'new', 'time': '2016-09-05 22:21:00'}
             ]


def question():
    n = 1
    for question in questions:
        Question.create(status=question['status'], time=question['time'], applicant=Applicant.select().
                        where(Applicant.id == n), question=question['question'])
        n += 1