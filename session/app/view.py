"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-07 13:19
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : view.py
  # @Software: PyCharm
"""

from . import app
from flask import request, render_template, session, redirect, url_for, make_response, abort
import time
from functools import wraps


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not 'user' in session:
            abort(401)
        return view_func(*args, **kwargs)

    return wrapper

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'admin login successfully'
        else:
            return 'no such user'

    if 'user' in session:
        response = make_response('hello {}'.format(session['user']), 200)

        return response
    else:
        title = request.args.get('title', 'Default')
        return render_template('login.html', title=title)


@app.route('/admin')
@login_required
def admin():
    return 'admin allowed'


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('login'))


@app.errorhandler(404)
def error(error):
    return 'page not found caoxin'

@app.errorhandler(401)
def error401(error):
    return 'user not login'


