import os
import re


module_name_re = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')


def valid_module_name(module_name):
    return module_name_re.match(module_name)


class Module(object):
    ##
    # Constructors
    @classmethod
    def from_file(cls, file_path):
        raise NotImplementedError('not yet implemented')

    def __init__(self, module_path):
        components = module_path.split('.')

        # Sanity check
        for module_path in components:
            if not all([valid_module_name(mod) for mod in components]):
                raise ValueError('Invalid module path: %s' % (module_path,))

        self.components = components

    @property
    def parents(self):
        if len(self.components) <= 1:
            return []
        return self.components[:-1]

    @property
    def module_name(self):
        return self.components[-1]

    def split(self):
        return (self.parents, self.module_name)

    @property
    def module_file(self):
        parents, last = self.split()
        return os.path.join(*parents + [last + '.py'])

    @property
    def package_file(self):
        parents, last = self.split()
        return os.path.join(*parents + [os.path.join(last, '__init__.py')])

    def is_package(self):
        return os.path.isfile(self.package_file)

    def is_module(self):
        return os.path.isfile(self.module_file)


    ##
    # Self-printing
    def __unicode__(self):  # noqa
        return u'Module %s' % (u'.'.join(self.components,))

    def __repr__(self):
        return 'Module(%r)' % (self.components,)

    def __str__(self):
        return unicode(self).encode('utf-8')
