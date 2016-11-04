#!/usr/bin/env python
# -- coding: utf-8 --
'''
File Name : interface.auth.views
Description :
Author : Raymond
change Activity :
create file : C:/Users/Raymond/git/testerlife/interface/auth/views.py
create time :2016年11月1日
'''

from interface.auth import api , Resource, auth
from flask import render_template , request
from interface import login, login_user, login_required , current_user , logout_user
from interface.db import User
from util.result.result import result
from werkzeug import redirect

@auth.route('/' , methods=['GET', 'POST'])
def homepage():
    return render_template('login.html')

@login.user_loader
def load_user(id):
    return User.query.filter_by(id=int(id)).first()


@api.resource('/login')
class Login(Resource):
    def post(self):
        args = request.form
        user = User.query.filter_by(username=args['username']).first()
        if user and user.userpassword == args['password']:
            login_user(user, True)
            return result.success()
        return result.error()

@api.resource('/logout')
class logout(Resource):
    @login_required
    def post(self):
        if current_user:
            logout_user()
        return result.success()

        
        
            
