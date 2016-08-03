import random
import string
from models import *



def passwordgen():
    passw = []
    for i in range(3):
        passw.append(random.choice(string.ascii_lowercase))
        passw.append(random.choice(string.ascii_uppercase))
        passw.append(random.choice(string.digits))
    random.shuffle(passw)
    a = "".join(passw)
    return a

b = []
for i in Applicant.select():
    b.append(i.application_code)


applicant = Applicant.find_missing_app_code()


def solution():
    passw = passwordgen()
    if passw not in b:
        return passw
    else:
        return solution()


def pw():
    for i in applicant:
        i.application_code = solution()
        i.status = 'in progress'
        i.save()
