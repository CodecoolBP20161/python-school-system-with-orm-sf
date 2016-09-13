# This script can create the database tables based on your models
from models import *
from example_data import *


db.connect()

db.drop_tables([Applicant, School, Mentor, Interview, AssignMentor, Question, EmailLog], safe=True)
db.create_tables([Applicant, School, Mentor, Interview, AssignMentor, Question, EmailLog], safe=True)

add_schools()
add_applicants()
add_mentors()
interview()
question()