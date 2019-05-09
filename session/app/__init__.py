"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-07 13:14
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : __init__.py
  # @Software: PyCharm
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    return app


app = create_app()

from . import view
