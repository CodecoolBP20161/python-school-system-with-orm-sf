from models import *



def filter_by_mentor_name():
    """Filter applicants by their mentor name"""
    mentor = input('Give me the mentor name: ')
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


def applicant_by_school_location():
    """Filter applicants by their school location"""
    choice = input("Choose a city where you want to see the students of the local school.\n[BP/ MI/ KR/ LA]: ")
    if choice == "BP":
        return list(Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 1))
    elif choice == "MI":
        return list(Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 2))
    elif choice == "KR":
        return list(Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 3))
    elif choice == "LA":
        return list(Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 4))


def applicant_by_location():
    choice = input("Enter a city where you want to search applicants: ")
    return list(Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.city == choice))


def filter_by_personal_data(first_name, last_name, city, email, status):
    """Filter applicants by their personal data"""
    print('Give the input what you wants, or leave it blank!')
    first_name =
    last_name =
    city =
    email =
    status =
    return Applicant.select().where((Applicant.first_name.contains(first_name)),
                                    (Applicant.last_name.contains(last_name)),
                                    (Applicant.city.contains(city)),
                                    (Applicant.email.contains(email)),
                                    (Applicant.status.contains(status)))
