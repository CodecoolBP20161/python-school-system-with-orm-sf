# This script can create the database tables based on your models
from models import *
from example_data import *


db.connect()

db.drop_tables([Applicant, City, School, Mentor, Interview, AssignMentor], safe=True)
db.create_tables([Applicant, City, School, Mentor, Interview, AssignMentor], safe=True)
add_schools()
add_applicants()
add_cities()
add_mentors()
interview()
assign_mentors()
