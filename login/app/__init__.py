"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-07 17:49
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : __init__.py
  # @Software: PyCharm
"""

from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    init_loginmanager(login_manager, app)

    register_blueprint(app)

    return app


def register_blueprint(app):
    '''
    register blueprint to flask application
    '''
    from .auth import auth_blueprint

    app.register_blueprint(auth_blueprint)


def init_loginmanager(login_manager, app):
    from .auth import AUTH_BLUEPRINT
    login_manager.init_app(app)

    # 如果未登陆的用户访问了一个只有登际用户才能访问的Url, 即被@login_required修饰的url
    # 那这次访问会被重定向到login_view定义的这个视图函数里，同时闪现由login_message定义的错误消息
    # 并且会在Url后添加?next=xxx，以便用户名和密码验证成功后跳转
    login_manager.login_view = AUTH_BLUEPRINT + '.login'
    login_manager.login_message = 'Unauthorized User'


print('in __init__.py')

app = create_app()

from . import helper



