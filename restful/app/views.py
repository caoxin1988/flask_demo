"""
  Created by Cao,Xin on 2019-05-13 13:46
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource
from app import api


USER_LIST = {
    '1': {'name': 'cat'},
    '2': {'name': 'tom'}
}


class UserList(Resource):
    def get(self):
        print(request.args.get('name'))
        return USER_LIST


    def post(self):
        user_id = int(max(USER_LIST.keys())) + 1
        user_id = '%i' % user_id
        USER_LIST[user_id] = {'name': request.form['name']}

        return USER_LIST


api.add_resource(UserList, '/users')


from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

class User(Resource):
    def get(self, user_id):
        return USER_LIST[user_id]

    def delete(self, user_id):
        USER_LIST.pop(user_id)

        return USER_LIST

    # def put(self, user_id):
    #     USER_LIST[user_id] = {'name': request.form['name']}
    #     return USER_LIST

    def put(self, user_id):
        args = parser.parse_args()
        USER_LIST[user_id] = {'name': args['name']}
        return USER_LIST


api.add_resource(User, '/user/<user_id>')

