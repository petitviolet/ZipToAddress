# -*- encoding:utf-8 -*-
'''
'''

# from flask.ext.sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

from sqlalchemy import (create_engine, MetaData, exc, event)
from sqlalchemy.pool import Pool
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config import DB_CONFIGURATION


engine = create_engine('mysql://{USER}:{PASSWD}@{HOST}/{DB}?charset=utf8'\
        .format(**DB_CONFIGURATION),\
        encoding='utf-8', echo=False, pool_size=15, pool_recycle=3600, \
        max_overflow=0, echo_pool=True)
Session = scoped_session(sessionmaker(\
        autocommit=False, autoflush=False, bind=engine))
# sessionはローカル変数、Sessionはグローバル変数として扱う
# session = Session()
metadata = MetaData(engine)
Base = declarative_base()
Base.query = Session.query_property()

@event.listens_for(Pool, "checkout")
def ping_connection(dbapi_connection, connection_record, connection_proxy):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("SELECT 1")
    except:
        raise exc.DisconnectionError()
    finally:
        cursor.close()


def drop_all():
    metadata.drop_all()


def create_all():
    metadata.create_all()


def remove_session():
    Session.remove()
