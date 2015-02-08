# -*- encoding:utf-8 -*-
''' logger configuration
'''
import logging
import logging.config
import yaml
from config import project_name

import os
basedir = os.path.abspath(os.path.dirname(__file__))

def logmaker():
    config = {
        'filename': basedir + '/log/zip_address.log',
        'when': 'D',
        'interval': 1,
        'backupCount': 14,
        # 'level': logging.DEBUG,
    }
    return logging.handlers.TimedRotatingFileHandler(**config)

# logging.config.fileConfig('config_logger.ini')
logger_config = yaml.load(open(basedir + '/config/config_logger.yaml').read())
logging.config.dictConfig(logger_config)
logger = logging.getLogger(project_name)
