from models import Applicant, School, Interview
from peewee import *


def filter_applicants(form, interview_ids):
    query = Applicant.select().join(School, JOIN.LEFT_OUTER).switch(Applicant).join(Interview, JOIN.LEFT_OUTER)
    if form.applicant_app_code.data != "":
        query = query.where(Applicant.application_code.contains(form.applicant_app_code.data))
    print(form.applicant_first_name.data)
    if form.applicant_first_name.data != "":
        query = query.where(Applicant.first_name.startswith(form.applicant_first_name.data))
    if form.applicant_last_name.data != "":
        query = query.where(Applicant.last_name.startswith(form.applicant_last_name.data))
    if form.applicant_email.data != "":
        query = query.where(Applicant.email.contains(form.applicant_email.data))
    if form.applicant_city.data != "":
        query = query.where(Applicant.city.startswith(form.applicant_city.data))
    if form.applicant_school.data != "":
        query = query.where(School.location.startswith(form.applicant_school.data))
    if form.applicant_interview.data != "":
        query = query.where(Interview.id << interview_ids)

    return query
