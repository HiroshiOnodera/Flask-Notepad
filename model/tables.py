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

    def verify(self, password):
        ''' check password
        '''
        if pbkdf2_sha256.verify(password, self.password):
            return True
        return False

    def __repr__(self):
        return '<user_id %r><email %r>' % (self.user_id, self.email)


class Memo(DB.Model):
    ''' Memo table
    '''
    memo_id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.user_id'), nullable=False)
    sentence = DB.Column(DB.String(1024), nullable=False)
    update_date = DB.Column(DB.Date, nullable=False)

    user = DB.relationship('User', backref=DB.backref('users', lazy=True))

    def __repr__(self):
        return '<memo_id %r><user_id %r><update_date %r>' \
            % (self.memo_id, self.user_id, self.update_date)
