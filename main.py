import os

from flask_migrate import Migrate
from models import db
from flask import Flask

from config import config

app_name = 'FLASK_CELERY_DEMO'

config_name = os.getenv('FLASK_CONFIG') or 'default'

app = Flask(app_name)
app_config = config[config_name]
app_config.init_app(app)

app.config.from_object(app_config)

db.init_app(app)
migrate = Migrate(app, db)


from api import api

api.init_app(app)
