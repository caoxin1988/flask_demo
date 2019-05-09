"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-08 09:54
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : __init__.py
  # @Software: PyCharm
"""

from flask import Blueprint

AUTH_BLUEPRINT = 'auth_blueprint'


auth_blueprint = Blueprint(AUTH_BLUEPRINT, __name__)

from . import auth
