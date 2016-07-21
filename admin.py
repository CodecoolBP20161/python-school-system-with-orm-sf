from models import *


def filter_by_mentor_name(mentor):
    try:
        first, last = mentor.split()
    except ValueError as error:
        print('Please provide the full name of the mentor separated with a space!', error)

    applicants = Applicant.select().join(Interview).join(Mentor).where(Applicant.interview_slot != False,
    Mentor.first_name == first, Mentor.last_name == last)
    if applicants:
        return applicants
    else:
        return('No associated applicants found to the given mentor!')
