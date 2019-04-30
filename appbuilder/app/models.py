from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)
    address =  Column(String(564), default='Street ')
    birthday = Column(Date)
    personal_phone = Column(String(20))
    personal_cellphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    contact_group = relationship("ContactGroup")

    def __repr__(self):
        return self.name


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {'contact_group':'Contacts Group'}
    list_columns = ['name','personal_cellphone','birthday','contact_group']

    show_fieldsets = [
                        (
                            'Summary',
                            {'fields': ['name', 'address', 'contact_group']}
                        ),
                        (
                            'Personal Info',
                            {'fields': ['birthday', 'personal_phone', 'personal_cellphone'], 'expanded': False}
                        ),
                     ]

class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


appbuilder.add_view(
    GroupModelView,
    "List Groups",
    icon = "fa-folder-open-o",
    category = "Contacts",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    ContactModelView,
    "List Contacts",
    icon = "fa-envelope",
    category = "Contacts"
)