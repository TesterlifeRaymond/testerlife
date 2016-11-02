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
    def success(api):
        return {'errMsg':None, 'result':'success', 'api':api}
    
    @staticmethod
    def error(errMsg, api, params):
        return {'errMsg':errMsg, 'result':'failed', 'api':api, 'params':str(params)}
