from models import *
from collections import OrderedDict
import admin

TITLES = ['id', 'first_name', 'last_name', 'city', 'school', 'application_code', 'interview_slot', 'status', 'email']

def print_query(object_list, titles):
    import itertools as IT

    data_frame = OrderedDict()
    print(data_frame)
    for i in range(len(titles)):
        datas = []
        for obj in object_list:
            datas.append(obj.__dict__['_data'][titles[i]])
        data_frame[titles[i]] = datas

    matrix = zip(*[value if isinstance(value, list) else IT.repeat(value) for key, value in data_frame.items()])
    print(''.join(['{:15}'.format(key) for key in data_frame.keys()]))
    for row in matrix:
        print(''.join(['{:15}'.format(str(item)) for item in row]))


def select_all_applicants():
    """Select all aplicants"""
    pass


def call_submenu():
    """Select applicants by filters"""
    menu_loop(admin_applicants_menu)


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
                print_query(obj_list, TITLES)
            except:
                pass


admin_applicants_menu = OrderedDict([
    ('1', admin.filter_by_mentor_name),
    ('2', admin.applicant_by_school_location),
    ('3', admin.filter_by_personal_data),
    ('4', admin.filter_by_personal_data)
])

admin_menu = OrderedDict([
    ('1', select_all_applicants),
    ('2', call_submenu)
])
