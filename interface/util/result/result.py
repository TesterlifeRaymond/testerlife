#!/usr/bin/env python
# -- coding: utf-8 --
'''
File Name : util.result.result
Description :
Author : Raymond
change Activity :
create file : C:/Users/Raymond/git/testerlife/util/result/result.py
create time :2016年11月3日
'''

class result:
    
    @staticmethod
    def success(userType=None):
        return {'errMsg':None, 'result':'success', 'userType':userType}
    
    @staticmethod
    def error(error):
        return {'errMsg':error, 'result':'invalid'}
