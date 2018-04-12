
'''
create Flask-Notepad

'''
# -*- coding: utf-8 -*-
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

    return app
