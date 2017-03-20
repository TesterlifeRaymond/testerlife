from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    """ user info tables models """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    uid = db.Column(db.String(64))
    hash_password = db.Column(db.String(256))

    def __repr__(self):
        """ return username models """
        return '<User %r>' % self.username

    @property
    def password(self):
        """ raise AttributeError('password cannot be read')  """
        raise AttributeError('password cannot be read')

    @password.setter
    def password(self, password):
        """ rewrite password for werwerkzeug models"""
        self.hash_password = generate_password_hash(password)

    def confirm_password(self, password):
        """confirm user password """
        return check_password_hash(self.hash_password, password)
