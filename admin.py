from models import *
import datetime


def filter_by_mentor_name():
    """Filter applicants by their mentor name"""
    mentor = input('Give me the full mentor name: ')
    try:
        first, last = mentor.split()
        applicants = (Applicant.select()
                      .join(Interview)
                      .join(Mentor)
                      .where(~(Applicant.interview_slot >> None),
                             Mentor.first_name.contains(first),
                             Mentor.last_name.contains(last)))
        if applicants:
            return applicants
        else:
            return ('No associated applicants found to the given mentor!')
    except ValueError as error:
        print('Please provide the full name of the mentor separated with a space!', error)


def applicant_by_school_location():
    """Filter applicants by their school location"""
    choice = input(
        "Choose a city where you want to see the students of the local school.\n[BP/ MI/ KR/ LA]: ")
    if choice == "BP":
        return list(Applicant.select().where(Applicant.school == 1))
    elif choice == "MI":
        return list(Applicant.select().where(Applicant.school == 2))
    elif choice == "KR":
        return list(Applicant.select().where(Applicant.school == 3))
    elif choice == "LA":
        return list(Applicant.select().where(Applicant.school == 4))


def applicant_by_status():
    """Filter applicants by their status"""
    choice = input("Enter a status [accepted/ rejected/ in progress]: ")
    return Applicant.select(Applicant.first_name, Applicant.last_name).where(Applicant.status == choice)


def filter_by_personal_data():
    """Filter applicants by their personal data"""
    print('Give the input what you wants, or leave it blank!')
    first_name = input('Enter first name (if you want): ')
    last_name = input('Enter last name (if you want): ')
    city = input('Enter city where the applicant live (if you want): ')
    email = input('Enter email (if you want): ')
    status = input('Enter status (if you want): ')
    return Applicant.select().where((Applicant.first_name.contains(first_name)),
                                    (Applicant.last_name.contains(last_name)),
                                    (Applicant.city.contains(city)),
                                    (Applicant.email.contains(email)),
                                    (Applicant.status.contains(status)))


def filter_by_time():
    """Filter applicants by their interview start time"""
    a = [int(x) for x in input(
        'Please type the correct start time (correct form: yyyy m d h m s): ').split()]
    input_len = len(a)
    if input_len < 6:
        i = input_len
        for i in range(6):
            a.append(1)
    time = datetime.datetime(a[0], a[1], a[2], a[3], a[4], a[5])
    if input_len == 1:
        return [i for i in Applicant.select(Interview, Applicant).join(Interview).where(Interview.start.year == time.year)]
    elif input_len == 2:
        return [i for i in Applicant.select(Interview, Applicant).join(Interview).where(Interview.start.year == time.year,
                                                                                        Interview.start.month == time.month)]
    elif input_len == 3:
        return [i for i in Applicant.select(Interview, Applicant).join(Interview).where(Interview.start.year == time.year,
                                                                                        Interview.start.month == time.month,
                                                                                        Interview.start.day == time.day)]
    elif input_len == 4:
        return [i for i in Applicant.select(Interview, Applicant)
                                    .join(Interview).where(Interview.start.year == time.year,
                                                           Interview.start.month == time.month,
                                                           Interview.start.day == time.day,
                                                           Interview.start.hour == time.hour
                                                           )]
    elif input_len == 5:
        return [i for i in Applicant.select(Interview, Applicant)
                                    .join(Interview).where(Interview.start.year == time.year,
                                                           Interview.start.month == time.month,
                                                           Interview.start.day == time.day,
                                                           Interview.start.hour == time.hour,
                                                           Interview.start.minute == time.minute
                                                           )]
    elif input_len == 6:
        return [i for i in Applicant.select(Interview, Applicant)
                                    .join(Interview).where(Interview.start.year == time.year,
                                                           Interview.start.month == time.month,
                                                           Interview.start.day == time.day,
                                                           Interview.start.hour == time.hour,
                                                           Interview.start.minute == time.minute,
                                                           Interview.start.second == time.second
                                                           )]


def interview_by_application_code():
    """Filter interviews by applicants app_code"""
    app_code = input('Please enter an applicatin code!: ')
    return Interview.select().join(Applicant).where(Applicant.application_code == app_code)


def interview_by_time():
    """Filter interviews by their interview start time"""
    a = [int(x) for x in input(
        'Please type the correct start time (correct form: yyyy m d h m s): ').split()]
    input_len = len(a)
    if input_len < 6:
        i = input_len
        for i in range(6):
            a.append(1)
        time = datetime.datetime(a[0], a[1], a[2], a[3], a[4], a[5])
    if input_len == 1:
        return [i for i in Interview.select().where(Interview.start.year == time.year)]
    elif input_len == 2:
        return [i for i in Interview.select().where(Interview.start.year == time.year,
                                                    Interview.start.month == time.month)]
    elif input_len == 3:
        return [i for i in Interview.select().where(Interview.start.year == time.year,
                                                    Interview.start.month == time.month,
                                                    Interview.start.day == time.day)]
    elif input_len == 4:
        return [i for i in Interview.select()
                                    .where(Interview.start.year == time.year,
                                           Interview.start.month == time.month,
                                           Interview.start.day == time.day,
                                           Interview.start.hour == time.hour
                                           )]
    elif input_len == 5:
        return [i for i in Interview.select()
                                    .where(Interview.start.year == time.year,
                                           Interview.start.month == time.month,
                                           Interview.start.day == time.day,
                                           Interview.start.hour == time.hour,
                                           Interview.start.minute == time.minute
                                           )]
    elif input_len == 6:
        return [i for i in Interview.select()
                                    .where(Interview.start.year == time.year,
                                           Interview.start.month == time.month,
                                           Interview.start.day == time.day,
                                           Interview.start.hour == time.hour,
                                           Interview.start.minute == time.minute,
                                           Interview.start.second == time.second
                                           )]


def interview_by_school():
    """Filter interviews by school"""
    choice = input("Enter a city where you want to search the scheduled interviews: ")
    interviews = Interview.select().join(Mentor).join(School).where(Interview.free == False, School.location == choice)
    if len(interviews) == 0:
        print("Sorry we didn't find this school in our system. Please try a new one.")
        return interview_by_school()
    return interviews


def interview_by_mentor():
    """Filter interviews by mentor name"""
    choice_first_name = input(" Please enter the first name of the mentor:  ")
    choice_last_name = input("Please enter the last name of the mentor:   ")
    mentor = Interview.select().join(Mentor).where(Mentor.first_name.contains(choice_first_name),
                                                      Mentor.last_name.contains(choice_last_name),
                                                      Interview.free == False)
    if len(mentor) == 0:
        print("sorry we didn't have mentor with this name")
        return interview_by_mentor()
    return mentor

def question_by_name():
    """Filter questions by mentor name"""
    choice_first_name = input(" Please enter the first name of the mentor:  ")
    choice_last_name = input("Please enter the last name of the mentor:   ")
    name = Question.select(Question.question, Applicant.first_name, Applicant.last_name).join(Applicant).join(Mentor)\
                            .where(Mentor.first_name.contains(choice_first_name),\
                                    Mentor.last_name.contains(choice_last_name))
    if len(name) == 0:
        print("Sorry, we didn't find.Please try a new one.")
        return question_by_name()
    return name













