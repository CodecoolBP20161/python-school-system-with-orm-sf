import smtplib
from config import Config
from decorate import logger


class Mail():
    fromaddr = Config.load("sender")
    username = Config.load("mail_username")
    password = Config.load("mail_password")

    @classmethod
    @logger
    def send(cls, message,receiver,subject):
        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (cls.fromaddr, receiver, subject, message)
        server = smtplib.SMTP(Config.load("server"))
        server.ehlo()
        server.starttls()
        try:
            server.login(cls.username, cls.password)
            server.sendmail(cls.fromaddr, receiver, msg.encode("UTF-8"))
            server.quit()
        except TypeError:
            print("Login creditentials are not properly set,please set them in config.json")
            exit()

    @staticmethod
    def format():
        pass
