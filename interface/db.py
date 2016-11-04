from interface import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import  UserMixin
db = SQLAlchemy(app)

class User(db.Model,UserMixin):
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
    
    def is_correct_password(self, password):
        if User.query.filter_by(userpassword = password):
            return True

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return self.username