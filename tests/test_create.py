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

    def test_create_dash_p(self):
        """Create with promote option "just promoted" when module already exists."""

        # Setup, let's create a simple module
        Module('foo.bar.qux').create()
        self.assertFileTree([
            'foo/__init__.py',
            'foo/bar/__init__.py',
            'foo/bar/qux.py'])

        # If we now "mkmodule -p foo.bar.qux", qux should simply be promoted
        Module('foo.bar.qux').create(promote=True)
        self.assertFileTree([
            'foo/__init__.py',
            'foo/bar/__init__.py',
            'foo/bar/qux/__init__.py'])
