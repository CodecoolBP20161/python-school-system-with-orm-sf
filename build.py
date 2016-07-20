# This script can create the database tables based on your models
from models import *

db.connect()

db.drop_tables([Applicant, City, School], safe=True)
db.create_tables([Applicant, City, School], safe=True)
