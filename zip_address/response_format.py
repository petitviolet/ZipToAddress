# -*- encoding:utf-8 -*-
from xml.sax.saxutils import escape as esacpe_xml
import json

def json_to_xml(json_obj):
    ''' convert dict to xml format string
    :param json_obj: dict type(if json string, json.loads)
    :returns xml formatted string
    '''
    result_list = list()
    obj_type = type(json_obj)

    if obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json_to_xml(sub_elem))
        return ''.join(result_list)

    if obj_type is dict:
        for tag, sub_obj in json_obj.items():
            result_list.append('<{t}>'.format(t=tag))
            result_list.append(json_to_xml(sub_obj))
            result_list.append('</{t}>'.format(t=tag))
        return ''.join(result_list)

    return esacpe_xml('{j}'.format(j=json_obj))

def convert_format(dict_result, to_xml=False):
    ''' dict型の値をjson/xmlに変換する
    :param dict_result: dict
    :param to_xml: True or False
    :returns json or xml format value
    '''
    if to_xml:
        result = json_to_xml(dict_result)
    else:
        result = json.dumps(dict_result)
    return result

