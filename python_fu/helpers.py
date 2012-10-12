from __future__ import with_statement
from .compat import u


def replace_extension(filename, new_extension):
    filename, ext = filename.rsplit(u('.'), 1)
    return u('.').join([filename, new_extension])


def touch_file(filename):
    with open(filename, 'a'):
        pass
