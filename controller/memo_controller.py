'''
memo
'''
# -*- encoding utf-8 -*-
import datetime
from flask import render_template, Blueprint, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_required
from model.tables import Memo
from form.memo_form import MemoForm


APP = Blueprint('memo_controller', __name__)
DB = SQLAlchemy()


@APP.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    ''' memo list
    '''
    memo = Memo.query.filter(Memo.user_id == current_user.user_id)
    form = MemoForm()
    return render_template('home.html', memo=memo, form=form)


@APP.route('/create_memo', methods=['POST'])
@login_required
def create_memo():
    ''' add new memo in memo table
    '''
    form = MemoForm()
    if not form.validate_on_submit():
        memo = Memo.query.filter(Memo.user_id == current_user.user_id)
        return render_template('home.html', memo=memo, form=form)

    new_memo = Memo()
    new_memo.user_id = current_user.user_id
    new_memo.sentence = form.sentence.data
    new_memo.update_date = datetime.date.today()

    DB.session.add(new_memo)
    DB.session.commit()

    memo = Memo.query.filter(Memo.user_id == current_user.user_id)
    form.sentence.data = ''
    return render_template('home.html', memo=memo, form=form)

@APP.route('/delete_memo/<int:memo_id>', methods=['POST'])
@login_required
def delete_memo(memo_id):
    ''' delete memo
    '''
    memo = DB.session.query(Memo).get(memo_id)
    DB.session.delete(memo)
    DB.session.commit()
    return redirect(url_for('memo_controller.home'))
