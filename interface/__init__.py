import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_restful import Api, Resource
from flask_vue import Vue
from interface import config


app = Flask(__name__)
app.config.from_object(config)
app.secret_key = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'
api = Api(app)
vue = Vue(app)
"""
    app.logger is project logging module
"""

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(name)s:%(lineno)d]'
))
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)


@app.route('/')
def reindex():
    return '跳转ing....'
