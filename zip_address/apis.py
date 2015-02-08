# -*- encoding:utf-8 -*-
''' API
'''
from logger import logger
from flask import (Blueprint, request, copy_current_request_context,
                   Response, redirect, url_for)
from urllib.parse import unquote
from threading import Thread
from config import project_name
from zip_address.controllers.zip import Zip
from zip_address.error_response import ErrorResponse

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
    return "test response"

@blueprint.route('/zip_search', methods=['GET'])
def zip_search():
    ''' zip search endpoint
    /zip_search?zip=123-4567
    '''
    zip = request.args.get('zip', '')
    logger.debug(zip)
    result = Zip.search(zip)
    if result is False:
        # invalid format
        return ErrorResponse.format_error()
    logger.debug(result)
    response = Response(result, mimetype='application/json')
    response.status_code = 200 if result else 204
    return response

