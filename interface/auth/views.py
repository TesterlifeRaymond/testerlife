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
from interface import login
from sqlalchemy.sql import and_
from interface.db import User
from util.result.result import result
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug import redirect

@auth.route('/' , methods=['GET', 'POST'])
def homepage():
    return render_template('login.html')

@login.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

@api.resource('/login')
class Login(Resource):
    def post(self):
        args = request.form
        user = User.query.filter_by(username=args['username']).first()
        if user and user.userpassword == args['password']:
            login_user(user,True)
            print(current_user.is_authenticated)
            return result.success()
        return result.error()

@auth.route('/logout')
def logout():
    print(current_user.is_authenticated)
    if current_user:
        logout_user()
    return redirect('/')
            
        
        
            
