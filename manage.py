#manage.py

from flask.ext.script import Manager
from score import app
from score.mailer import Mailer
from score.toolbox import russian_plurals

manager = Manager(app)

@manager.command
def mail_test():
    Mailer.welcome_mail()

@manager.command
def test_russian_plurals():
    for n in range(0,125):
        print ("%d %s назад" %(n, russian_plurals('секунда', n, ago=True)))



if __name__ == "__main__":
    manager.run()
