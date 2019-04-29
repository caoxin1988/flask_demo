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
$ export FLASK_APP=app
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

## 2. flask-babel
