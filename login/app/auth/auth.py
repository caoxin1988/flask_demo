"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-07 18:42
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : auth.py
  # @Software: PyCharm
"""

from . import auth_blueprint, AUTH_BLUEPRINT
from app.helper.user_loader import query_user
from flask import request, flash, redirect, url_for, render_template, session
from flask_login import (current_user, login_required, login_user, logout_user, fresh_login_required)
from app.libs.User import User
from app import login_manager


@auth_blueprint.route('/index')
@login_required
def index():
    return 'Logged in as: %s' % current_user.get_id()


@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        user = query_user(username)

        if user and request.form.get('password') == user['password']:
            curr_user = User()
            curr_user.id = username     # 最后会放到session['user_id']中

            login_user(curr_user, remember=True)
            # login_user(curr_user)

            return redirect(url_for(AUTH_BLUEPRINT + '.index'))

        flash('Wrong username or password!')

    print(session['user_id'])

    return render_template('login.html', login=AUTH_BLUEPRINT + '.login')


@auth_blueprint.route('/home')
@login_required
def home():
    return render_template('hello.html')


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logged out successfully!'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'
