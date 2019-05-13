"""
  Created by Cao,Xin on 2019-05-13 13:12
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Api, Resource


api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    api.init_app(app)

    return app


app = create_app()


from app import views


api.init_app(app)

