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

from interface.auth import api , Resource

@api.resource('/')
class HelloWorld(Resource):
    def get(self):
        return "Hello World !"

