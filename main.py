'''
Flask-Notepad

this application store your memo using Flask
'''
# -*- coding: utf-8 -*-

from os import path
import click
from app import create_app
from model.tables import User, DB

APP = create_app(path.dirname(__file__) + '/config/config.cfg')


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
