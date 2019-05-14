"""
  Created by Cao,Xin on 2019-05-13 16:29
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    return app


app = create_app()

socketio.init_app(app)


from app import views


