from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    userpassword = db.Column(db.String(100))

    def __init__(self, username=None, userpassword=None):
        self.username = username
        self.set_password(userpassword)

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return '<hash_password %s>' % self.userpassword



    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)
