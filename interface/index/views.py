#!/usr/bin/env python
# -- coding: utf-8 --
'''
File Name : interface.auth.views
Description :
Author : Raymond
change Activity :
create file : C:/Users/Raymond/git/testerlife/interface/auth/views.py
create time :2016�?11�?1�?
'''

from flask import render_template
from flask_login import login_required
from . import api , index


@index.route('/' , methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

