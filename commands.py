# -*- encoding:utf-8 -*-
''' manage.pyで呼ばれるコマンドを定義する
すでに稼働してるDB使ってるので、Testだけ使えるようにしている
'''
from flask.ext.script import Command


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
                        '--cover-erase --cover-package=app --verbose')
        convert_coverage = 'pyenv exec coverage html --include \'app/*\''
        open_result = ('open ./htmlcov/index.html')
        import os
        print('Start tests...')
        result = os.system('pyenv exec {}'.format(nosetests))
        os.system(convert_coverage)

        print('Complete Test.')
        if result == 0:
            os.system(open_result)
