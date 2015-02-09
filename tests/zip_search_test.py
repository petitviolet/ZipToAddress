# -*- encoding:utf-8 -*-
''' tests for /zip/<zip code>
'''
import unittest
from zip_address import app
import json


class ZipSearchTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.url = '/zip/{zip}'
        self.valid_zip_single = '001-0000'
        self.valid_zip_multiple = '001-0011'
        self.invalid_zip_not_found = '001-0001'
        self.invalid_zip_format = '0010011'

    def tearDown(self):
        del self.app

    def _get_result(self, zip):
        ''' alias to get result
        '''
        return self.app.get(self.url.format(zip=zip))

    def test_valid_zip_single(self):
        ''' test valid zip code returns 1 result
        '''
        result = self._get_result(self.valid_zip_single)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.headers.get('Content-Type'), 'application/json')
        address = json.loads(result.data.decode('utf-8'))
        self.assertEqual(len(address), 1)

    def test_valid_zip_multiple(self):
        ''' test valid zip code returns multiple results
        '''
        result = self._get_result(self.valid_zip_multiple)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.headers.get('Content-Type'), 'application/json')
        addresses = json.loads(result.data.decode('utf-8'))
        self.assertEqual(len(addresses) > 1, True)

    def test_invalid_zip_not_found(self):
        ''' test invalid zip code returns no result
        '''
        result = self._get_result(self.invalid_zip_not_found)
        self.assertEqual(result.status_code, 204)
        self.assertEqual(result.headers.get('Content-Type'), 'application/json')

    def test_invalid_zip_format(self):
        ''' test invalid zip code format error
        '''
        result = self._get_result(self.invalid_zip_format)
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.headers.get('Content-Type'), 'application/json')
