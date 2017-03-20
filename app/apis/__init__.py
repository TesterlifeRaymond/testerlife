
"""
@Author: liujinjia
@Date:   2017-03-06 11:03:09
@Project : doraemon
@File : __init__.py
@Last Modified by:   liujinjia
@Last Modified time: 2017-03-06 14:57:24
"""
from flask import Blueprint

API = Blueprint('api_1_0', __name__)

from . import apis
