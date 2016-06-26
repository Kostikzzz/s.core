from . .db import db
from flask.ext.login import UserMixin
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

from . .config import ADMIN_EMAILS

# import os
# from . .path import ROOT_DIR, UPLOAD_FOLDER, AVATAR_FOLDER
from . .logger import StrangersLog


class User (UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    g_username = db.Column(db.String(50))
    f_username = db.Column(db.String(50))
    t_username = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(100), unique=True)
    google_id =db.Column(db.String(255), unique=True)
    facebook_id =db.Column(db.String(255), unique=True)
    twitter_id =db.Column(db.String(255), unique=True)
    image =db.Column(db.String(250), unique=True)
    last_login = db.Column(db.DateTime)
    worker = db.Column(db.Boolean, default = False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def register(username, password):
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def register_google_user(username, email, google_id):
        if username == '':
            username = email
        user = User(g_username=username, nickname=username, email=email, google_id=google_id)
        db.session.add(user)
        db.session.commit()
        StrangersLog.write('google_sign_up')
        return user

    @staticmethod
    def register_facebook_user(username, email, facebook_id):
        if username == '':
            username = email
        user = User(f_username=username, nickname=username, email=email, facebook_id=facebook_id)
        db.session.add(user)
        db.session.commit()
        StrangersLog.write('fb_sign_up')
        return user

    def __repr__(self):
        return '<User {0}>'.format(self.nickname)

    def is_admin(self):
        return (self.email in ADMIN_EMAILS)

    # def get_avatar(self):
    #     if self.image:
    #         return os.path.join(ROOT_DIR, UPLOAD_FOLDER, AVATAR_FOLDER, self.image)
    #     else:
    #         return os.path.join(ROOT_DIR, UPLOAD_FOLDER, AVATAR_FOLDER, 'noname_avatar.png')


