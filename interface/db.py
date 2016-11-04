from interface import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

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

