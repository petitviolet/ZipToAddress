# -*- encoding:utf-8 -*-
''' configuration file
'''

from datetime import timedelta
import os
import yaml
project_name = "zip_address"
basedir = os.path.abspath(os.path.dirname(__file__))

# modelsで使ってる
database_config_fname = basedir + '/config/config_database.yaml'
if os.path.exists(database_config_fname):
    DB_CONFIGURATION = yaml.load(open(database_config_fname).read())
else:
    DB_CONFIGURATION = yaml.load(open(database_config_fname + '.travis').read())

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False

    CSRF_ENABLED = True
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
