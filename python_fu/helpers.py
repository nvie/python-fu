def replace_extension(filename, new_extension):
    filename, ext = filename.rsplit('.', 1)
    return '.'.join([filename, new_extension])
