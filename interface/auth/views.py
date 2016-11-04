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
from flask import render_template , request, url_for, redirect
from interface import login
from util.result.result import result

@auth.route('/' , methods=['GET', 'POST'])
def homepage():
    return render_template('login.html')

@api.resource('/login')
class Login(Resource):
    def post(self):
        args = request.form
        if args['username'] == '123':
            return {"result":"success"}
        return {"result":"invalid"}
