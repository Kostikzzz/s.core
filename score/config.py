MAINTENANCE = False
DEPLOYED = False

ADMIN_EMAILS = ['k.lapshov@gmail.com',]


#KDB EXAMPLE
GOOGLE_ID = "567089266746-srim9s6rn1dgjgqqqcpj4f3mcr6ae62j.apps.googleusercontent.com"
GOOGLE_SECRET = "6K7yTYIt2at8Z80tOCrj5f9Q"

FACEBOOK_APP_ID = "562185260616101"
FACEBOOK_APP_SECRET="df81015fc4c1c0b9eb2afda078994f4b"

BOOKING_ID = "356391"

SECRET_KEY = "itsasecret"



if DEPLOYED:
    USER = 'Kostikzzz'
    PASS = 'Rpoack4710'
    HOST = 'Kostikzzz.mysql.pythonanywhere-services.com'
    BASE = 'Kostikzzz$db.score'
    SOCKET = ''
    DEBUG = False
else:
    USER = 'root'
    PASS = 'root'
    HOST = 'localhost'
    BASE = 'db.score'
    SOCKET = '/Applications/MAMP/tmp/mysql/mysql.sock'
    DEBUG = True

socket=''
if SOCKET !='':
    socket = '?unix_socket='+SOCKET

DBURI = 'mysql://%s:%s@%s/%s%s' % (USER, PASS, HOST, BASE, socket)


