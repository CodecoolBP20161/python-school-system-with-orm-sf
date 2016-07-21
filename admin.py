from models import *


def applicant_by_school_location():
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
        return Applicant.select().where((Applicant.first_name.contains(first_name)),
                                        (Applicant.last_name.contains(last_name)),
                                        (Applicant.city.contains(city)),
                                        (Applicant.email.contains(email)),
                                        (Applicant.email.contains(email)))
