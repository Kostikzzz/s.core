#manage.py

from flask.ext.script import Manager

manager = Manager(app)

@manager.command
def test_command():
    print ("test ok")



if __name__ == "__main__":
    manager.run()
