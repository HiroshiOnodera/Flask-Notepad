'''
login
'''
# -*- encoding utf-8 -*-
from flask import render_template, Blueprint, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required, current_user
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
        current_app.logger.info('Accessed by a nonexistent user , user email : %r' \
        %(form.email.data))
        return render_template('login.html', form=form)

    if not users.verify(password):
        current_app.logger.info('No matching password , user id : %r' %(users.user_id))
        return render_template('login.html', form=form)

    user = LoginUser()
    user.id = users.user_id
    login_user(user)
    current_app.logger.info('login success , user id : %r' %(users.user_id))
    return redirect(url_for('memo_controller.home'))

@APP.route("/logout")
@login_required
def logout():
    '''logout
    '''
    current_app.logger.info('logout  , user id : %r' %(current_user.user_id))
    logout_user()
    return redirect(url_for('login_controller.top'))
