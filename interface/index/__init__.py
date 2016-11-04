#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    register index blueprint 
"""
from flask import Blueprint
from flask_restful import Api


index = Blueprint('index', __name__, template_folder='templates', static_folder='assets')
api = Api(index)

from . import views
