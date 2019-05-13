"""
  Created by Cao,Xin on 2019-05-09 17:58
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import app, db
from app.models.User import User
from app.models.Score import Score
from flask import request


@app.route('/delete')
def delete():

    name = request.args.get('name')

    print(name)

    user = User.query.filter_by(name=name).first()
    print(user)
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            print('successfully')
            return 'delete successfully'
        except Exception as e:
            print(e)
            db.session.rollback()

    return 'delete failed'


@app.route('/add')
def add():
    try:
        db.session.add(User('tom', 18))
        db.session.add(User('cat', 20))
        db.session.commit()
    except Exception as e:
        print(e)
        return 'add error'

    return 'add successfully'


@app.route('/update')
def update():
    User.query.filter_by(name='tom').update({'age': User.age+1})
    db.session.commit()

    return 'update successfully'


@app.route('/find')
def find():
    # users = User.query.all()
    # print(users)

    user = User.query.filter(User.age>17).all()
    print(user)

    return 'find successfully'


@app.route('/score_add')
def score_add():

    user = User.query.filter_by(name='tom').first()
    if user:
       db.session.add(Score('Math', 80.5, user))
       db.session.add(Score('Art', 95, user))
       db.session.commit()

    return 'score add successfully'


@app.route('/score_find')
def score_find():
    name = request.args.get('name')

    user = User.query.filter_by(name=name).first()
    if user:
        for score in user.scores:
            print('name {}, course: {}, score: {};'.format(score.name, score.course, score.score))

    return 'score find successfully'

