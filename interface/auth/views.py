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
from util.result.result import result


@auth.route('/')
def get():
    return render_template('index.html')

@api.resource('/login')
class Login(Resource):
    def post(self):
        args = request.form
        return result.error(errMsg='Login Error', api='/auth/login', params=args)
