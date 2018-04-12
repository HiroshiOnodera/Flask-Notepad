'''
login
'''
# -*- encoding utf-8 -*-
from flask import render_template, Blueprint, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user
from flask_login import LoginManager
from form.login_form import LoginForm
from model.user_model import User
from model.login_user_model import LoginUser

APP = Blueprint('login_controller', __name__)
DB = SQLAlchemy()
LOGIN_MANAGER = LoginManager()

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
    '''
    未認証ユーザのアクセス制御
    セッション無効
    '''
    return redirect(url_for('login_controller.top'))

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
    return render_template('home.html', form=form)
