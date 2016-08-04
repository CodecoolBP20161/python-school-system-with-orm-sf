import smtplib
from config import Config


class Mail():
    fromaddr = Config.load("sender")
    username = Config.load("mail_username")
    password = Config.load("mail_password")

    @classmethod
    def send(cls, message,receiver,subject):
        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (cls.fromaddr, receiver,subject, message)
        server = smtplib.SMTP(Config.load("server"))
        server.ehlo()
        server.starttls()
        server.login(cls.username, cls.password)
        server.sendmail(cls.fromaddr, receiver, msg.encode("UTF-8"))
        server.quit()

    @staticmethod
    def format():
        pass

Mail.send("hello", 'carbalage@gmail.com', 'test')
