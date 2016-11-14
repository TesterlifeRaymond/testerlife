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

from flask import render_template,url_for
from flask_login import login_required
from flask_restful import Resource
from . import api, admin
from ..util.result.result import result

@api.resource('/login')
class login(Resource):
    @staticmethod
    def get():
        return result.success('None')


@admin.route('/')
def login_index():
    return render_template('creditease.html')
