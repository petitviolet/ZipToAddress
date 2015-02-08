# -*- encoding:utf-8 -*-
'''
'''
from logger import logger
from flask import (Blueprint, request, copy_current_request_context,
                   Response, redirect, url_for)
from urllib.parse import unquote
from threading import Thread
from config import project_name

blueprint = Blueprint(project_name, __name__)

# def use_session(func):
#     def inner(*args, **kwargs):
#         with Session() as session:
#             func(*args, session=session, **kwargs)
#     return inner

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@blueprint.route('/', methods=['GET'])
def index():
    return "hello7"
