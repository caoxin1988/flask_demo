"""
  Created by Cao,Xin on 2019-05-10 18:39
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from datetime import datetime
from app import db

print('in score')


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(50))
    access_date = db.Column(db.DateTime)
    score = db.Column(db.Float)
    name = db.Column(db.String(50))
    is_access = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('scores', lazy='dynamic'))

    def __init__(self, course, score, user, assess_date=None):
        self.course = course
        self.score = score
        self.is_pass = (score >= 60)
        if assess_date is None:
            assess_date = datetime.now()
        self.name = user.name
        self.assess_date = assess_date
        self.user = user

    def __repr__(self):
        return '<Course %r of User %r>' % (self.course, self.user.name)


