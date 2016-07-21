from models import *
import datetime


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


def applicant_by_school_location():
    choice = input("Choose a city where you want to see the students of the local school.\n[BP/ MI/ KR/ LA]: ")
    if choice == "BP":
        return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 1)
    elif choice == "MI":
        return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 2)
    elif choice == "KR":
        return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 3)
    elif choice == "LA":
        return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.school == 4)


def applicant_by_location():
    choice = input("Enter a city where you want to search applicants: ")
    return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.city == choice)


def applicant_by_status():
    choice = input("Enter a status [accepted/ rejected/ in progress]: ")
    return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.status == choice)


def filter_by_personal_data(first_name, last_name, city, email, status):
    return Applicant.select().where((Applicant.first_name.contains(first_name)),
                                    (Applicant.last_name.contains(last_name)),
                                    (Applicant.city.contains(city)),
                                    (Applicant.email.contains(email)),
                                    (Applicant.email.contains(status)))


def filter_by_time():
    a = [int(x) for x in input('Please type the start time (correct form: yyyy m d h m s)').split()]
    if len(a)<6:
        i = len(a)
        for i in range(6):
            a.append(1)
    time = datetime.datetime(a[0], a[1], a[2], a[3], a[4], a[5])
    return Applicant.select(Interview, Applicant).join(Interview).where(Interview.start == time)

