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

from interface.index import api , Resource, index
from flask import render_template , request

@index.route('/' , methods=['GET', 'POST'])
def index():
    return render_template('index.html')

