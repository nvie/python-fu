from __future__ import absolute_import
from .helpers import SandboxedTestCase
from python_fu.module import Module


class TestCreateModule(SandboxedTestCase):
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
