"""
  Created by Cao,Xin on 2019-05-09 17:16
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<User %r>' % self.name
