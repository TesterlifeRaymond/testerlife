"""
# -*- coding: utf-8 -*-
# @Author: liujinjia
# @Date:   2017-03-21 06:34:16
# @Last Modified by:   liujinjia
# @Last Modified time: 2017-03-21 06:34:21
"""

from flask_restful import Resource


class BaseResponse:
    """格式化返回结果"""
    def __init__(self):
        """ pass"""
        self.result = None
        self.message = None
        self.response = None

    def set_res(self, **kwargs):
        """ 构造返回结构函数 """
        self.result = kwargs.get('result')
        self.message = kwargs.get('message')
        self.response = kwargs.get('response')

class BaseResource(Resource):
    """ 继承Resource 类，构造一个返回类 """
    def __init__(self):
        """ 初始化返回函数 """
        self.base_res = BaseResponse()
