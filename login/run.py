"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-05-07 18:54
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : run.py
  # @Software: PyCharm
"""

from app import app

if __name__ == '__main__':
    print('in main')
    app.run(debug=True)
