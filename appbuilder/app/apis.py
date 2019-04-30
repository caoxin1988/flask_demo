"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-04-30 11:08
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : apis.py
  # @Software: PyCharm
"""
from flask import request
from flask_appbuilder.api import BaseApi, expose, rison, safe
from flask_appbuilder.security.decorators import protect

from . import appbuilder

greeting_schema = {"type": "object", "properties": {"name": {"type": "string"}}}


class ExampleApi(BaseApi):

    @expose('/greeting')
    def greetingdd(self):
       return self.response(200, message='hello greeting')


appbuilder.add_api(ExampleApi)
