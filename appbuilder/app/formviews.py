"""
  # -*- coding: utf-8 -*-
  # @Time    : 2019-04-29 16:49
  # @Author  : Cao,Xin
  # @Email   : caoxin1988s@gmail.com
  # @File    : formviews.py
  # @Software: PyCharm
"""
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _
from flask import flash

from . import appbuilder


class MyForm(DynamicForm):
    field1 = StringField(('Field1'),
        description=('Your field number one!'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    field2 = StringField(('Field2'),
        description=('Your field number two!'), widget=BS3TextFieldWidget())

class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message1 = 'My form submitted'

    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(self.message1, 'info')

appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                     category="My Forms", category_icon="fa-cogs")
