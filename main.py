from models import *


def print_applicant_table():
    for applicant in Applicant.select():
        print('application code: %s\nfirst name: %s\nlast_name: %s\ncity: %s\nschool: %s'
              % (applicant.application_code,
                 applicant.first_name,
                 applicant.last_name,
                 applicant.city,
                 applicant.school))

print_applicant_table()
input()
Applicant.set_app_code()
print_applicant_table()
input()
Applicant.finding_city()
print_applicant_table()