'''
config object
'''
# -*- coding: utf-8 -*-

from os import urandom


class DevelopmentConfig():
    ''' Use in development environment
    '''
    #SECRET_KEY is used csrf key in flask-wtf and flask-login
    SECRET_KEY = urandom(24)
