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

from flask import render_template , request, current_app
from flask_restful import Resource

from interface.util.result.result import result
from . import api , auth
from .. import login, login_user, login_required , current_user , logout_user
from ..model import User



@login.user_loader
def load_user(user_id):
    try:
        user = User.query.get(int(user_id))
        return user
    except:
        return None

@auth.route('/' , methods=['GET', 'POST'])
def index():
    return render_template('login.html')

@api.resource('/login')
class login(Resource):
    def post(self):
        args = request.form
        user = User.query.filter_by(username=args.get('username')).first()
        if user and user.userpassword == args.get('password'):
            login_user(user, True)
            return result.success()
        return result.error()

@api.resource('/logout')
class logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return result.success()
