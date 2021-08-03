import os
from os import getenv
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # SERVER_NAME = "appname"
    DEBUG = False
    SECRET_KEY = "sdfscaukvwjh3489o2y9rt87h'/.;'/.l;/.'"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@10.10.32.63/ftest"
    REDIS_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_BROKER_URL = REDIS_URL


    @classmethod
    def init_app(cls, app):
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
