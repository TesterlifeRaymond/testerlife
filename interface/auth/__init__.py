#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    register auth blueprint 
"""
from flask import Blueprint, request
from flask_restful import Api, Resource


auth = Blueprint('auth', __name__, template_folder='templates',
                 static_folder='assets')
api = Api(auth)
from interface.auth import views
