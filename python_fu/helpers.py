from __future__ import with_statement


def replace_extension(filename, new_extension):
    filename, ext = filename.rsplit('.', 1)
    return '.'.join([filename, new_extension])


def touch_file(filename):
    with open(filename, 'a'):
        pass
