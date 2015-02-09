# -*- encoding:utf-8 -*-
'''
'''
import unittest
from zip_address import app
import json

class IndexTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.url = '/'

    def tearDown(self):
        del self.app

    def test_index(self):
        ''' test index
        '''
        result = self.app.get(self.url)
        self.assertEqual(json.loads(result.data.decode('utf-8')), {'result': 'test response'})
        self.assertEqual(result.headers.get('Content-Type'), 'application/json')
