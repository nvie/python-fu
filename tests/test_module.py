from __future__ import absolute_import
import unittest
from python_fu.module import Module


class TestModule(unittest.TestCase):
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