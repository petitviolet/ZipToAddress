# -*- encoding:utf-8 -*-
''' Commands called by manage.py
'''
from flask.ext.script import (Command, Option)
import sys


class CreateDB(Command):
    """
    Creates sqlalchemy database
    """
    def run(self):
        pass
        # from database import create_all
        # create_all()


class DropDB(Command):
    """
    Drops sqlalchemy database
    """
    def run(self):
        pass
        # from database import drop_all
        # drop_all()

class Test(Command):
    def run(self):
        nosetests = ('nosetests tests/*.py --with-xunit --with-coverage '
                        '--cover-erase --cover-package=zip_address --verbose')
        convert_coverage = 'pyenv exec coverage html --include \'app/*\''
        open_result = ('open ./htmlcov/index.html')
        import os
        print('Start tests...')
        result = os.system('pyenv exec {}'.format(nosetests))
        os.system(convert_coverage)

        print('Complete Test.')
        if result == 0:
            os.system(open_result)

class TestTravis(Command):
    def run(self):
        import os
        os.system('nosetests --with-coverage --cover-erase '
                  '--cover-package=zip_address')

class GunicornServer(Command):
    ''' Run the app within Gunicorn
    '''
    def __init__(self, host='127.0.0.1', port=8000, workers=4):
        self.port = port
        self.host = host
        self.workers = workers

    def get_options(self):
        return [
            Option('-h', '--host',
                   dest='host',
                   default=self.host),
            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),
            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=self.workers),
        ]

    # def handle(self, app, host, port, workers):
    def run(self, host, port, workers):
        import os
        os.system('pyenv exec gunicorn zip_address:app -w {w} -b {h}:{p}'\
                 .format(w=workers, h=host, p=port))
