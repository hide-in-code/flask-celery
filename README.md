# 一个集成flask 和 celery的任务调度管理api demo，可在代码之上扩充您的代码，来快速实现任务调度


## 安装项目依赖

    pip install -r requirements.txt


## 启动开发环境服务

### export flask env

    export FLASK_APP=main.py
    export FLASK_ENV=development 


### DB初始化

在初始化前，需要先删除掉db文件和migrations文件夹。

    flask db init
    flask db migrate
    flask db upgrade


### 启动web server

    flask run


### 启动redis-server

    redis-server --port 6379

### 启动celery worker

    celery worker -A celeryapp.task.celery_app


#### 发起新任务

    http post http://127.0.0.1:5000/api/tasks

#### 查看所有的任务

    http http://127.0.0.1:5000/api/tasks

## TODO
- pytest
- webUI 
