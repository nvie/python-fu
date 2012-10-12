from __future__ import absolute_import
import os
import unittest
from tempfile import mkdtemp
from shutil import rmtree


def walk_files():
    for root, _, files in os.walk('.'):
        for file in sorted(files):
            yield os.path.normpath(os.path.join(root, file))


class SandboxedTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = mkdtemp()
        self.cwd = os.getcwd()
        os.chdir(self.tmpdir)
        self.addCleanup(os.chdir, self.cwd)
        self.addCleanup(rmtree, self.tmpdir)

    def assertFileTree(self, list_of_files):
        actual_file_list = list(walk_files())
        self.assertItemsEqual(actual_file_list, list_of_files)
