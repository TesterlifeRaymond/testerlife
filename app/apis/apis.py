"""
# @Author: liujinjia
# @File Name:/home/ray/git/testerlife/app/apis/apis.py 
# @Create by:   Ray
# @Create time: 2017年3月21日 上午6:40:24  
"""
from flask_restful import Api
from . import API
from .resource.login import Login

API = Api(API)
API.add_resource(Login, '/login')