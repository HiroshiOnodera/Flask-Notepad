'''
user model
'''
# -*- encoding utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

DB = SQLAlchemy()

class User(DB.Model):
    ''' User table
    '''
    user_id = DB.Column(DB.Integer, primary_key=True)
    password = DB.Column(DB.String(256), unique=False, nullable=False)
    email = DB.Column(DB.String(120), unique=True, nullable=False)

    def hash_password(self, password):
        ''' hashed password
        '''
        self.password = pbkdf2_sha256.hash(password)

    def __repr__(self):
        return '<user_id %r><email %r>' % (self.user_id, self.email)
