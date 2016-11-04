from flask_login import  UserMixin
from . import db

db.create_all()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    userpassword = db.Column(db.String(100))

    def __init__(self, username=None, userpassword=None):
        self.username = username
        self.userpassword = userpassword

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return '<Password %s>' % self.userpassword
    
    def is_correct_password(self, password):
        if User.query.filter_by(userpassword=password):
            return True
