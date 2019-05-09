"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-08 13:46
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : user_loader.py
  # @Software: PyCharm
"""


'''
for test, we use a list to save users and password
we'll move these into database later
'''

from app import login_manager
from app.libs.User import User


users = [
    {'username': 'tom', 'password': '111111'},
    {'username': 'admin', 'password': '123456'}
]


def query_user(username):
    """
    query username from database
    :param
        username: name of the user
    :return:
        a dict contains username and password
    """
    for user in users:
        if username == user['username']:
            return user
    return None


@login_manager.user_loader
def load_user(username):
    """
    if username is exist, return a User object
    else return None
    """
    print('==== load_user ====')
    if query_user(username):
        cur_user = User()
        cur_user.id = username

        return cur_user
