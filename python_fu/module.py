import os
import re
from .helpers import touch_file, replace_extension
from .commandline import info, warning
from .compat import PY3, u


module_name_re = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')


def valid_module_name(module_name):
    return (module_name_re.match(module_name) and
            not (module_name.startswith('__') and module_name.endswith('__')))  # exclude __init__ and __main__


class Module(object):
    ##
    # Constructors
    @classmethod
    def from_file(cls, file_path):
        raise NotImplementedError('not yet implemented')

    def __init__(self, module_path):
        components = module_path.split('.')

        # Sanity check
        if not all([valid_module_name(mod) for mod in components]):
            raise ValueError('Invalid module path: %s' % (module_path,))

        self.components = components

    @property
    def module_path(self):
        return u('.').join(self.components)

    @property
    def parent_components(self):
        if len(self.components) <= 1:
            return []
        return self.components[:-1]

    @property
    def parent_module(self):
        if len(self.components) <= 1:
            return None
        return Module('.'.join(self.components[:-1]))

    @property
    def module_name(self):
        return self.components[-1]

    def split(self):
        return (self.parent_components, self.module_name)

    @property
    def module_file(self):
        parents, last = self.split()
        return os.path.join(*parents + [last + '.py'])

    @property
    def module_dir(self):
        parent = self.parent_module
        if not parent:
            return '.'
        return parent.package_dir

    @property
    def package_file(self):
        return os.path.join(self.package_dir, '__init__.py')

    @property
    def package_dir(self):
        return os.path.join(*self.components)

    def is_package(self):
        return os.path.isfile(self.package_file)

    def is_module(self):
        return os.path.isfile(self.module_file)

    def exists(self):
        return self.is_package() or self.is_module()

    def create(self, promote=False):
        parent_module = self.parent_module
        if parent_module:
            parent_module.create(promote=True)

        if self.exists():
            # This module exists already, so we're done, unless we need to
            # promote it now.
            if not self.is_package() and promote:
                self.promote()

            return

        # If it does not exist, we need to create it now.  We may assume the
        # parent directory exists by now.
        if not os.path.exists(self.module_file):
            touch_file(self.module_file)

        # It's a bit of a short-hand, but it works for now
        if promote:
            self.promote()

    def promote(self):
        if self.is_package():
            warning('%s is a package already, skipping.' % (self,))
            return

        if not self.is_module():
            warning('%s does not exist, skipping.' % (self,))
            return

        module_file = self.module_file
        package_file = self.package_file

        #info('Found %s' % (module_file,))
        info('Promoting %s -> %s' % (module_file, package_file))
        os.renames(module_file, package_file)

        compiled_extensions = ['pyo', 'pyc']
        for ext in compiled_extensions:
            filename = replace_extension(module_file, ext)
            if os.path.isfile(filename):
                info('Cleaning up compiled self file %s' % (filename,))
                os.remove(filename)

    def demote(self):
        if self.is_module():
            warning('%s is a non-package module already, skipping.' % (self,))
            return

        if not self.is_package():
            warning('%s does not exist, skipping.' % (self,))
            return

        module_file = self.module_file
        package_file = self.package_file

        # Sanity check: only allow demotes for packages that contain an
        # __init__.py file, and nothing else
        pkgdir = os.path.dirname(package_file)
        package_files = set(os.listdir(pkgdir))
        allowed_junk = set(['__init__.pyc', '__init__.pyo', '.DS_Store'])

        superflous = package_files - allowed_junk - set(['__init__.py'])
        if superflous:
            warning('Directory %r is not empty. Cannot demote, skipping.' % (pkgdir,))
            for file in superflous:
                warning('- %s' % (file,))
            return

        for junkfile in allowed_junk:
            junkfile = os.path.join(pkgdir, junkfile)
            if os.path.isfile(junkfile):
                info('Cleaning up junk file %s' % (junkfile,))
                os.remove(junkfile)

        #info('Found %s' % (module_file,))
        info('Moving %s -> %s' % (package_file, module_file))
        os.rename(package_file, module_file)

        # Remove the package directory, if it's empty
        os.rmdir(pkgdir)


    ##
    # Self-printing
    if not PY3:  # noqa
        def __unicode__(self):
            return self.module_path

        def __str__(self):
            return unicode(self).encode('utf-8')
    else:
        def __str__(self):  # noqa
            return self.module_path
