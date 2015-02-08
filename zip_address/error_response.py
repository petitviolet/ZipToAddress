# -*- encoding:utf-8 -*-
''' aliases for error response
'''
from flask import Response
from zip_address.response_format import convert_format

class ErrorResponse(object):
    XML_FORMAT = 'text/xml'
    JSON_FORMAT = 'application/json'

    def response(self, status_code, message, format='json'):
        ''' make error response body
        :param status_code: http status code
        :param message: error message
        :param format: json or xml
        :returns flask.Response
        '''
        to_xml = format == 'xml'
        mimetype = self.JSON_FORMAT if not to_xml else self.XML_FORMAT

        res_dict = {'result': {'code': status_code, 'error': message}}
        content = convert_format(res_dict, to_xml)

        response = Response(content, mimetype=mimetype)
        response.status_code = status_code
        return response

    @classmethod
    def unauthorized(cls, message=None, format='json'):
        ''' Unauthorized response
        '''
        status_code = 401
        message = message if message else 'Unauthorized'
        return cls.response(cls, status_code, message, format=format)

    @classmethod
    def forbidden(cls, message=None, format='json'):
        ''' Forbidden response
        '''
        status_code = 403
        message = message if message else 'Forbidden'
        return cls.response(cls, status_code, message, format=format)

    @classmethod
    def format_error(cls, message=None, format='json'):
        ''' Format Error response
        '''
        status_code = 400
        message = message if message else 'Format Error'
        return cls.response(cls, status_code, message, format=format)
