# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

applicants = [
    {'first_name': 'Kata', 'last_name': 'Kiss', 'city': 'Budapest'},
    {'first_name': 'Zoltán', 'last_name': 'Nagy', 'city': 'Miskolc'}
]


def add_applicants():
    for applicant in applicants:
        Applicant.create(first_name=applicant['first_name'], last_name=applicant['last_name'], city=applicant['city'])
