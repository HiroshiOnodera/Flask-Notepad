'''
Login from
'''
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    ''' login validation
    '''
    email = StringField('email', [
        DataRequired(),
        Email()
    ], render_kw={
        'placeholder': 'メールアドレス'
    })

    password = PasswordField('password', [
        DataRequired(),
        Length(min=8, max=256)
    ], render_kw={
        'placeholder': 'パスワード'
    })
