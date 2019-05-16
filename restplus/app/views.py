"""
  Created by Cao,Xin on 2019-05-15 15:28
  Any suggesstions, please send mail to caoxin1988s@gmail.com
"""

# -*- coding: utf-8 -*-

from app import app, api
from flask_restplus import Resource, fields, reqparse, marshal
from flask import request


@api.route('/hello', '/world')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        api.abort(403)


parser = reqparse.RequestParser()
parser.add_argument('data', type=int, required=True, help='data should be int')
parser.add_argument('id', type=int, required=True, help='id should be int')

@api.route('/index')
class Index(Resource):
    def get(self):
        return {'id': '{}'.format(id)}

    def post(self):
        args = parser.parse_args()
        data, id = args['data'], args['id']

        return {'data': data, 'id': id}


# model = api.model('Model', {
#     'idddd': fields.String(attribute='id'),
#     'task': fields.String
# })

model = api.model('Model', {
    'id': fields.String,
    'task': fields.String
})


class Dao():
    def __init__(self, id, task):
        self.id = id
        self.task = task
        self.status = 'done'


@api.route('/todo')
class Todo(Resource):
    @api.marshal_with(model)
    def get(self):
        return Dao(id='1', task='drink milk')


@api.route('/test')
class Test(Resource):
    def get(self):
        resource_fields = {'name': fields.String, 'first_names': fields.List(fields.String)}
        data = {'name': 'tom', 'first_names': ['zhang', 'wang']}
        # return marshal(data, resource_fields)
        return data
