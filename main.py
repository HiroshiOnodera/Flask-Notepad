'''
Flask-Notepad

this application store your memo using Flask
'''
# -*- coding: utf-8 -*-

from os import path
import click
from flask import redirect, url_for
from flask_login import LoginManager
from app import create_app
from model.tables import User, DB
from model.login_user_model import LoginUser

APP = create_app(path.dirname(__file__) + '/config/config.cfg')

LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.init_app(APP)

@LOGIN_MANAGER.user_loader
def user_loader(user_id):
    '''
    flask-login
    user loader
    '''
    user = LoginUser.query.get(int(user_id))
    return user


@LOGIN_MANAGER.unauthorized_handler
def unauthorized():
    ''' No sessions
    '''
    return redirect(url_for('login_controller.top'))


@APP.cli.command()
def initdb():
    ''' flask shell
    create tables.
    '''
    click.echo('start init db')
    click.echo('drop all tables')
    DB.drop_all()
    click.echo('create all tables')
    DB.create_all()
    click.echo('finish')


@APP.cli.command()
@click.argument('email')
@click.argument('password')
def useradd(email, password):
    ''' flask shell
    insert user table.
    '''

    click.echo('email ' + email + ', password ' + password)
    user = User()
    user.email = email
    user.hash_password(password)
    DB.session.add(user)
    DB.session.commit()
    click.echo('finish')
