"""
  Created by Cao,Xin on 2019-05-13 16:58
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import app, socketio


if __name__ == '__main__':
    socketio.run(app, debug=True)

# gunicorn --worker-class eventlet -w 1 app:app
