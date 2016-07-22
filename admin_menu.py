from models import *
from collections import OrderedDict
import admin


def print_query(object_list, titles):
    import itertools as IT

    data_frame = OrderedDict()
    for i in range(len(titles)):
        datas = []
        for obj in object_list:
            if titles[i] == 'interview_slot':
                interview_start = [iv for iv in Interview.select()
                                                         .where(Interview.id == obj.__dict__['_data'][titles[i]])]
                if interview_start:
                    datas.append(interview_start[0].start)
                else:
                    datas.append('None')

            elif titles[i] == 'school':
                school_location = [iv for iv in School.select()
                                                      .where(School.id == obj.__dict__['_data'][titles[i]])]
                if school_location:
                    datas.append(school_location[0].location)
                else:
                    datas.append('None')
            else:
                datas.append(obj.__dict__['_data'][titles[i]])
        data_frame[titles[i]] = datas

    matrix = zip(*[value if isinstance(value, list) else IT.repeat(value) for key, value in data_frame.items()])
    print(''.join(['{:15}'.format(key) for key in data_frame.keys()]))
    for row in matrix:
        print(''.join(['{:15}'.format(str(item)) for item in row]))


def select_all_applicants():
    """Show all applicants"""
    return Applicant.select()


def select_all_interviews():
    """Show all interview slots"""
    return Interview.select()


def call_applicant_submenu():
    """Select applicants by filters"""
    menu_loop(admin_applicants_menu)

def call_interview_submenu():
    """Select interviews by filters"""
    menu_loop(admin_interview_menu)



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
    ('4', admin.filter_by_time)
])

admin_menu = OrderedDict([
    ('1', select_all_applicants),
    ('2', select_all_interviews),
    ('3', call_applicant_submenu),
    ('4', call_interview_submenu)
])

admin_interview_menu = OrderedDict([
    ('1', admin.interview_by_school),
    ('2', admin.interview_by_applicant),
    ('3', admin.interview_by_mentor),
    ('4', admin.interview_by_date)
])
