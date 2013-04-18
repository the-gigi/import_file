import_file
===========

Python has an elaborate import mechanism that relies on a search path (sys.path) + lots of fancy hooks. But, sometimes you just need to import a module that is not on the search path and adding ots of fancy hooks. But, sometimes you just need to import a module that is not on the search path. The import_file() function lets you do that without complications and/or polluting sys.path.

It works by temporarily adding the file's parent dir to sys.path importing the file and immediately removing the parent dir form sys.path.

Note, that Python's relative import feature doesn't work for this use case and is designed for modules that reside in sub-directories of the same package.

## Usage:

    m = import_file('../../module.py')
    m.foo()

Check out also the test script: test.py for even more explict usage.
Enjoy!
