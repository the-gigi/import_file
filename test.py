__author__ = 'gigi'
import os
import shutil
from import_file import import_file


def test():
    try:
        os.makedirs('a/b/c')
        shutil.copy('module.py', 'a/b/c')
        assert os.path.isfile('a/b/c/module.py')

        m = import_file('a/b/c/module.py')
        assert m.__doc__ == 'This is a module for testing import_file'
        assert m.x == 5
        assert m.__author__ == 'gigi'
        m.prettify({'4': '5', 'a': range(5), 'b': 'c'})
    finally:
        shutil.rmtree('a')

if __name__ == '__main__':
    test()