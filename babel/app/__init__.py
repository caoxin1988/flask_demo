"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-05 16:19
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : __init__.py
  # @Software: PyCharm
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext, ngettext, lazy_gettext, refresh


def create_app():
    app = Flask(__name__, static_folder='templates')
    app.config.from_object('app.config')

    init_babel(app)

    return app


def init_babel(app):
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        return 'zh'

    @babel.timezoneselector
    def get_timezone():
        return 'UTC'


app = create_app()


@app.route('/hello')
def hello():
    hello = lazy_gettext('lazy text')
    return gettext('hello, China')


@app.route('/')
def index():
    return render_template('index.html')


from flask_babel import format_datetime
from datetime import datetime


@app.route('/time')
def time():
    return format_datetime(datetime.now())

from flask_babel import format_currency


@app.route('/money')
def money():
    return format_currency('123.5')
