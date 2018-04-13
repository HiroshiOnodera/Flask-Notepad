
'''
memo from
'''
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class MemoForm(FlaskForm):
    ''' memo validation
    '''
    sentence = StringField('sentence', [
        DataRequired(),
        Length(min=1, max=1024)
    ], render_kw={
        'placeholder': 'メモをつくる',
        'class' : 'sentence'
    })
