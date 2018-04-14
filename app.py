
'''
create Flask-Notepad

'''
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller import login_controller, memo_controller

def create_app(config_filename):
    ''' initialize flaks app
    '''
    app = Flask(__name__)
    app.config.from_object('config.config.DevelopmentConfig')
    app.config.from_pyfile(config_filename)
    app.register_blueprint(login_controller.APP)
    app.register_blueprint(memo_controller.APP)
    SQLAlchemy(app)

    #setup logging
    handler = RotatingFileHandler('./logs/app.log', maxBytes=100000, backupCount=10)
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    return app
