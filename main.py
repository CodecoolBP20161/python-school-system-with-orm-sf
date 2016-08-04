from models import *
from admin_menu import *

def print_applicant_table():
    for applicant in Applicant.select():
        print('\napplication code: %s\nfirst name: %s\nlast_name: %s\ncity: %s\nschool: %s\ninterview: %s\nstatus: %s'
              % (applicant.application_code,
                 applicant.first_name,
                 applicant.last_name,
                 applicant.city,
                 applicant.school,
                 applicant.interview_slot,
                 applicant.status))

print_applicant_table()
input()
Applicant.set_app_code()
print_applicant_table()
input()
Applicant.finding_city()
print_applicant_table()
input()
Applicant.assign_interview_slot()
print_applicant_table()


menu = True
while menu:
    menu_loop(main_menu)
    menu = False