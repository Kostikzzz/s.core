# from flask.ext.mail import Message, Mail

# mail = Mail()


# class Mailer():
#     def welcome_mail():
#         msg = Message('Добро пожаловать на KUDABY.RU', sender = 'info@kudaby.ru', recipients = ['k.lapshov@gmail.com'])
#         msg.body = ''
#         msg.html = '<h1>Добро пожаловать на KUDABY.RU</h1><h2>Мы рады вас видеть</h2>'
#         mail.send(msg)


from flask.ext.emails import Message

class Mailer():
    def welcome_mail():
        message = Message(html='<html><h1>Привет!</h1><h2>Добро пожаловать на КУДАБЫ.РУ</h2>',
                  subject="Добро пожаловать!",
                  mail_from=("КУДАБЫ", "info@kudaby.ru"))
        r = message.send(to=("k.lapshov@gmail.com"))