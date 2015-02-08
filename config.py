# -*- encoding:utf-8 -*-
'''
'''

from datetime import timedelta
import os
import yaml
project_name = "zip_address"
basedir = os.path.abspath(os.path.dirname(__file__))

# modelsで使ってる
DB_CONFIGURATION = yaml.load(open(basedir + '/config/config_database.yaml').read())

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False

    CSRF_ENABLED = True
    # セッションキー的なもの
    SECRET_KEY = os.urandom(24)
    LOGGER_NAME = "%s_log" % project_name
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    BLUEPRINTS = [
        'zip_address'
    ]

class Test(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class Dev(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
