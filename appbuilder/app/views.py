from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, expose, BaseView, has_access

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""

class MyView(BaseView):
    default_view = 'method1'

    @expose('/method1/')
    def method1(self):
        # do something with param1
        # and return it
        return 'Hello'

    @expose('/method2/<string:param1>')
    def method2(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        return param1

    @expose('/method3/<string:param>')
    def method3(self, param):
        param = 'goodbye {}'.format(param)

        return self.render_template('method3.html', param=param)

# appbuilder.add_view_no_menu(MyView())
appbuilder.add_view(MyView, 'Method1', category='My View')
appbuilder.add_link('Method2', href='/myview/method2/john', category='My View')
# appbuilder.add_link('method3', href='/myview/method3/xyz', category='My View')
# appbuilder.add_view(MyView, 'method3', category='My View')

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
