'''
Flask-Notepad

this application store your memo using Flask
'''
# -*- coding: utf-8 -*-

from os import path
from flask import render_template
from app import create_app
from form.login_form import LoginForm

APP = create_app(path.dirname(__file__) + '/config/config.cfg')

@APP.route('/')
def login_page():
    ''' view login page
    '''
    form = LoginForm()
    return render_template('login.html', form=form)
