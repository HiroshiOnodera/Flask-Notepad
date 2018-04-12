
'''
create Flask-Notepad

'''
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename):
    ''' initialize flaks app
    '''
    app = Flask(__name__)
    app.config.from_object('config.config.DevelopmentConfig')
    app.config.from_pyfile(config_filename)
    SQLAlchemy(app)
    return app
