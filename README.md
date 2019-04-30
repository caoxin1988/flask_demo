some flask demos for flask

## 1. flask-appbuilder

### 1.1 环境与依赖包

```
	$ pipenv --python 3.7
	$ pipenv shell
	$ pipenv install flask-appbuilder
```

安装flask-appbuilder包过程中，会同时安装一些别的包，比如flask, flask-babel等之类的包。

### 1.2 构建

在flask-appbuilder 2.2.x版本之后，fabmanager命令将会被丢弃，将可以使用flask fab [commands]代替。这里我们仍将使用fabmanager命令。

```
$ fabmanager create-app  ## 之后输入你想要的项目文件夹名, 并会提示你选择需要对接的数据库引擎
  Your new app name: first_app
  Your engine type, SQLAlchemy or MongoEngine [SQLAlchemy]:
  Downloaded the skeleton app, good coding!
$ cd first_app
$ flask fab create-admin
  Username [admin]:
  User first name [admin]:
  User last name [user]:
  Email [admin@fab.org]:
  Password:
  Repeat for confirmation:
```

之后将会把flask-appbuilder的框架代码从[这里](https://github.com/dpgaspar/Flask-AppBuilder-Skeleton.git)下载到刚才填写的first_app这个目录下。

### 1.3 运行

使用如下命令运行这个demo:

> python run.py

或者使用如下命令运行：

>$ export FLASK_APP=app  
 $ python -m flask run
 
 
### 1.4 关于Demo

views.py : 基于BaseView可以做出灵活性最大的界面，完全自定义界面的html, js等。  
formview.py : 基于FormViews做出表单类型的界面。这里会有表单验证  
models.py : 基于ModelView做出和数据库交户的界面，可以基于表单展示数据库中的数据，往数据库里提交数据。

* related_views: 可以使用tab来展示数据库中条件相关的其它信息。

apis.py: 基于BaseApi做RESTful api。

> 这里需要注意的是，flask-appbuilder的官方文档中demo有点问题，缺少@expose这个装饰器。

### 1.5 多语言

在babel文件夹下添加文件babel.cfg，并添加以下内容：

```
[python: **.py]
[jinja2: **/templates/**.html]
encoding = utf-8
```

建立不同语言翻译的初始文件：

```
$ pybabel init -i ./babel/messages.pot -d app/translations -l zh
```

执行后会在translations目录下创建zh/LC_MESSAGES/messages.po文件。接着执行

```
$ flask fab babel-extract
```

然后更改messages.po文件里英语对应的翻译：

```
$ flask fab babel-compile
```

之后会在messages.po文件同级目录下生成messages.mo文件。这个文件将最终被flask代码使用。



## 2. flask-babel
