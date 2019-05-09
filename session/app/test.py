"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-07 16:15
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : test.py
  # @Software: PyCharm
"""

from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        '''wrapper'''
        print('in wrapper')
        func()

    return wrapper


@decorator
def fun():
    '''fun'''
    print('in fun')


fun()

print(fun.__name__)
print(fun.__doc__)


