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
    def success():
        return {'errMsg':None, 'result':'success'}
    
    @staticmethod
    def error():
        return {'errMsg':"Login Error", 'result':'invalid'}
