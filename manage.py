#manage.py

from flask.ext.script import Manager
from score import app
from score.mailer import Mailer
manager = Manager(app)

@manager.command
def mail_test():
    Mailer.welcome_mail()



if __name__ == "__main__":
    manager.run()
