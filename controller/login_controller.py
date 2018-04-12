'''
login
'''
# -*- encoding utf-8 -*-
from flask import render_template, Blueprint, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user
from form.login_form import LoginForm
from model.tables import User
from model.login_user_model import LoginUser

APP = Blueprint('login_controller', __name__)
DB = SQLAlchemy()

@APP.route('/')
def top():
    ''' view login page
    '''
    form = LoginForm()
    return render_template('login.html', form=form)

@APP.route('/login', methods=['POST'])
def login():
    ''' user login
    '''
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    email = form.email.data
    password = form.password.data
    users = User.query.filter(User.email == email).first()

    if not users:
        return render_template('login.html', form=form)

    if not users.verify(password):
        return render_template('login.html', form=form)

    user = LoginUser()
    user.id = users.user_id
    login_user(user)
    return redirect(url_for('memo_controller.home'))
