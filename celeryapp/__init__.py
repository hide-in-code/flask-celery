import os

from flask_migrate import Migrate
from models import db
from flask import Flask

from config import config

from celery import Celery

app_name = 'FLASK_CELERY_DEMO'

config_name = os.getenv('FLASK_CONFIG') or 'default'

app = Flask(app_name)
app_config = config[config_name]
app_config.init_app(app)

app.config.from_object(app_config)

db.init_app(app)
migrate = Migrate(app, db)

celery_app = Celery(
    app.import_name,
    backend=app.config['CELERY_RESULT_BACKEND'],
    broker=app.config['CELERY_BROKER_URL']
)
celery_app.conf.update(app.config)

class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery_app.Task = ContextTask
