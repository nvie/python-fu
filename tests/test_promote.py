from __future__ import absolute_import
from .helpers import SandboxedTestCase, create_dummy_file, file_sha
from python_fu.module import Module


class TestPromotion(SandboxedTestCase):
    def test_module_promote(self):
        """Modules can be promoted."""
        Module('foo').create()
        self.assertFileTree(['foo.py'])

        Module('foo').promote()
        self.assertFileTree(['foo/__init__.py'])

        Module('bar').create()
        self.assertFileTree(['foo/__init__.py', 'bar.py'])

    def test_module_promote_removes_compiled_files(self):
        """Modules can be promoted."""
        Module('foo').create()
        create_dummy_file('foo.py', 'print "Hello"')
        create_dummy_file('foo.pyc', 'SENTINEL')
        self.assertFileTree(['foo.py', 'foo.pyc'])

        Module('foo').promote()
        self.assertFileTree(['foo/__init__.py'])  # pyc file removed

    def test_module_promotion_preserves_contents(self):
        """Promotion preserves file content."""
        create_dummy_file('foo.py', 'print "Hello, world"')
        sha1 = file_sha('foo.py')
        self.assertFileTree(['foo.py'])

        Module('foo').promote()
        self.assertFileTree(['foo/__init__.py'])
        sha2 = file_sha('foo/__init__.py')

        assert sha1 == sha2
