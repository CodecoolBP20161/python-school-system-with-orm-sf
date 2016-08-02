from models import *
from collections import OrderedDict
import admin
from tabulate import tabulate


def print_query(object_list, titles):
    import os

    vars = []
    for i in object_list.sql()[1]:
        vars.append(i)
    vars = tuple(vars)
    q_sql_with_pars = '"' + object_list.sql()[0] + '"'
    q_sql = q_sql_with_pars % vars
    for i in object_list.sql()[1]:
        if i is None:
            q_sql = q_sql.replace('None', 'Null')
        elif i == '%%':
            q_sql = q_sql.replace(i, "'" + "%" + "'")
        elif isinstance(i, str):
            q_sql = q_sql.replace(i, "'" + i + "'")
    os.system('psql -c ' + q_sql)


def select_all_applicants():
    """Show all applicants"""
    return Applicant.select(*admin.selection_dict['applicant_without_school'])


def select_all_interviews():
    """Show all interview slots"""
    return Interview.select(*admin.selection_dict['interview']).join(AssignMentor, JOIN.LEFT_OUTER).join(Mentor, JOIN.LEFT_OUTER)


def call_applicant_submenu():
    """Select applicants by filters"""
    menu_loop(admin_applicants_menu)


def call_interview_submenu():
    """Select interviews by filters"""
    menu_loop(admin_interview_menu)


def call_question_submenu():
    """Select question by filters"""
    menu_loop(admin_question_menu)


def menu_loop(menu):
    choice = None
    while choice != 'q':
        print("\nEnter q to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))

        choice = input('Action: ').lower().strip()

        if choice in menu:
            obj_list = menu[choice]()
            print('')
            try:
                titles = []
                titles.extend(obj_list[0].__dict__['_data'].keys())
                print_query(obj_list, titles)
            except:
                pass


admin_applicants_menu = OrderedDict([
    ('1', admin.filter_by_mentor_name),
    ('2', admin.applicant_by_school_location),
    ('3', admin.filter_by_personal_data),
    ('4', admin.filter_by_time),
    ('5', admin.applicant_by_status)
])

admin_menu = OrderedDict([
    ('1', select_all_applicants),
    ('2', select_all_interviews),
    ('3', call_applicant_submenu),
    ('4', call_interview_submenu),
    ('5', call_question_submenu)
])

admin_interview_menu = OrderedDict([
    ('1', admin.interview_by_school),
    ('2', admin.interview_by_application_code),
    ('3', admin.interview_by_mentor),
    ('4', admin.interview_by_time)
])

admin_question_menu = OrderedDict([
    ('1', admin.question_by_status),
    ('2', admin.question_by_name),
    ('3', admin.question_by_school),
    # ('4', admin.question_by_school),
    # ('5', admin.question_by_mentor_name)
])