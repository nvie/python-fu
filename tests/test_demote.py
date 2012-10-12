from __future__ import absolute_import
from .helpers import SandboxedTestCase
#from .helpers import create_dummy_file, file_sha
from python_fu.module import Module


class TestDemotion(SandboxedTestCase):
    def test_module_demote(self):
        """Packages can be demoted."""
        Module('foo').create(promote=True)
        self.assertFileTree(['foo/__init__.py'])

        Module('foo').demote()
        self.assertFileTree(['foo.py'])

    def test_nested_module_demote(self):
        """Nested packages can be demoted."""
        Module('foo.bar.qux').create(promote=True)
        self.assertFileTree([
            'foo/__init__.py',
            'foo/bar/__init__.py',
            'foo/bar/qux/__init__.py',
            ])

        Module('foo.bar.qux').demote()
        self.assertFileTree([
            'foo/__init__.py',
            'foo/bar/__init__.py',
            'foo/bar/qux.py',
            ])
