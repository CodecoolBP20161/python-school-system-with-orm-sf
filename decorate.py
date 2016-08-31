import datetime


modes = {'mentor': 'Interview details', 'applicant Interview': 'Interview time',
         'applicant Details': 'Application details'}

def logger(func):
    def inner(*args, **kwargs):
        from models import EmailLog, Mentor, Applicant
        subject = args[3]
        content = args[1][:144]
        mode = [i for i in modes if modes[i] == subject][0]
        recipient_email = args[2]
        if mode == 'mentor':
            mentor = Mentor.get(Mentor.email == recipient_email)
            recipient_name = mentor.first_name + " " + mentor.last_name
        else:
            applicant = Applicant.get(Applicant.email == recipient_email)
            recipient_name = applicant.first_name + " " + applicant.last_name

        timestamp = datetime.datetime.now()

        ret = func(*args, **kwargs)

        if ret is None:
            EmailLog.create(subject=subject, content=content, mode=mode, timestamp=timestamp,
                            recipient_name=recipient_name, recipient_email=recipient_email, status=True)
        else:
            EmailLog.create(subject=subject, content=content, mode=mode, timestamp=timestamp,
                            recipient_name=recipient_name, recipient_email=recipient_email, status=True)

    return inner
