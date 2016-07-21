from models import *


def filter_by_personal_data(first_name, last_name, city, email, status):
        return Applicant.select().where((Applicant.first_name.contains(first_name)),
                                        (Applicant.last_name.contains(last_name)),
                                        (Applicant.city.contains(city)),
                                        (Applicant.email.contains(email)),
                                        (Applicant.email.contains(email)))