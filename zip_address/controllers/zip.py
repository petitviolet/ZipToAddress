# -*- encoding:utf-8 -*-
''' zip code controller
'''
from zip_address.models.addr import AdAddress
from zip_address.response_format import convert_format
import re
zip_regex = re.compile(r'\d{3}-\d{2,4}')

class Zip(object):
    @classmethod
    def search(cls, zip):
        ''' zip code search
        :param zip: given zip code
        :returns json formatted SQL result
        '''
        is_valid = cls.validate_zip(zip)
        if not is_valid:
            return False
        result = AdAddress.query.filter(AdAddress.zip == zip)
        if result.count():
            data = [r.to_dict() for r in result.all()]
            return convert_format(data, False)
        else:
            return None

    @classmethod
    def validate_zip(cls, zip):
        ''' zip code validator
        :param zip: given zip code
        :returns True or False
        '''
        if len(zip) != 8:
            return False
        if not zip_regex.findall(zip):
            return False
        return True
