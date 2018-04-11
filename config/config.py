'''
config object
'''
# -*- coding: utf-8 -*-

from os import urandom


class DevelopmentConfig():
    ''' Use in development environment
    '''
    #SECRET_KEY is used csrf key in flask-wtf
    SECRET_KEY = urandom(24)
