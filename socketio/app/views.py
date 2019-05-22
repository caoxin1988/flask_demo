"""
  Created by Cao,Xin on 2019-05-14 08:50
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-
import random
from flask import render_template
from flask_socketio import emit, send
import time

from app import app, socketio

thread = None

import eventlet
eventlet.monkey_patch()


def background_task():
    while True:
        socketio.sleep(5)
        print('background task emit')
        t = random.randint(1, 100)
        socketio.emit('mess', {'data': t},
                      namespace='/test_conn')


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect', namespace='/test_conn')
def test_connect():
    global thread
    print('in test_connect')

    if thread is None:
        thread = socketio.start_background_task(target=background_task)


@socketio.on('my event', namespace='/test_conn')
def test_connect(message):
    time.sleep(20)
    print('test_connect', message)

    emit('my ev', message)

@socketio.on('my event broadcast', namespace='/test_conn')
def test_connect(message):

    emit('my ev broadcast', message, broadcast=True)
