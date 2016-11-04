#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    register auth blueprint 
"""
from flask import Blueprint
from flask_restful import Api

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='assets')
api = Api(auth)

from . import views