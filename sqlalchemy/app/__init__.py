"""
  Created by Cao,Xin on 2019-05-09 16:48
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# this MUST be imported before db.create_all()
from app import models


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    db.init_app(app)
    db.create_all(app=app)

    return app


app = create_app()


from . import views

