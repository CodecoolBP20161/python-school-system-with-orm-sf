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
