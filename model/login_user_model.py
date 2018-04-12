
'''
user model
'''
# -*- encoding utf-8 -*-

from flask_login import UserMixin
from model.user_model import User

class LoginUser(UserMixin, User):
    '''
    flask-login
    login user object
    '''
    pass
