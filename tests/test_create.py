from __future__ import absolute_import
from .helpers import SandboxedTestCase
import hashlib
from python_fu.module import Module


def create_dummy_file(filename, contents='print "Hello, world!"\n'):
    with open(filename, 'w') as f:
        f.write(contents)


def file_sha(filename):
    sha1 = hashlib.sha1()
    with open(filename, 'r') as f:
        sha1.update(f.read())
    return sha1.hexdigest()


class TestCreateModule(SandboxedTestCase):
    def test_invalid_module_names(self):
        """Invalid module names raise Exceptions."""
        with self.assertRaises(ValueError):
            Module('')

        with self.assertRaises(ValueError):
            Module('names-with-dashes')

        with self.assertRaises(ValueError):
            Module('names with spaces')

        with self.assertRaises(ValueError):
            Module('names.with,punctuations!')

        with self.assertRaises(ValueError):
            Module('4names_starting_with_numbers')

    def test_module_initialization(self):
        """Modules can be initialized with strings."""
        m = Module('foo')
        assert unicode(m) == 'foo'

        m = Module('foo.bar')
        assert unicode(m) == 'foo.bar'

        m = Module('foo.bar.qux')
        assert unicode(m) == 'foo.bar.qux'

    def test_module_get_parent(self):
        """Parent modules can be accessed from any module."""
        m = Module('foo')
        assert m.parent_module is None

        m = Module('foo.bar')
        assert unicode(m.parent_module) == 'foo'

        m = Module('foo.bar.qux')
        assert unicode(m.parent_module) == 'foo.bar'
        assert unicode(m.module_name) == 'qux'

    def test_module_promote(self):
        """Modules can be promoted."""
        Module('foo').create()
        self.assertFileTree(['foo.py'])

        Module('foo').promote()
        self.assertFileTree(['foo/__init__.py'])

        Module('bar').create()
        self.assertFileTree(['foo/__init__.py', 'bar.py'])

    def test_module_promotion_preserves_contents(self):
        """Promotion preserves file content."""
        create_dummy_file('foo.py')
        sha1 = file_sha('foo.py')
        self.assertFileTree(['foo.py'])

        Module('foo').promote()
        self.assertFileTree(['foo/__init__.py'])
        sha2 = file_sha('foo/__init__.py')

        assert sha1 == sha2

    def test_module_create(self):
        """Parent modules can be accessed from any module."""
        Module('foo').create()
        self.assertFileTree(['foo.py'])

        Module('bar').create()
        self.assertFileTree(['foo.py', 'bar.py'])

        Module('qux').create(promote=True)
        self.assertFileTree(['foo.py', 'bar.py', 'qux/__init__.py'])

        Module('foo.bar').create()
        self.assertFileTree(['foo/__init__.py', 'foo/bar.py', 'bar.py', 'qux/__init__.py'])
