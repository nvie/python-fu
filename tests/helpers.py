from __future__ import absolute_import, with_statement
import os
import hashlib
import unittest
from tempfile import mkdtemp
from shutil import rmtree


def walk_files():
    for root, _, files in os.walk('.'):
        for file in sorted(files):
            yield os.path.normpath(os.path.join(root, file))


def create_dummy_file(filename, contents=''):
    with open(filename, 'w') as f:
        f.write(contents)


def file_sha(filename):
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        sha1.update(f.read())
    return sha1.hexdigest()


class SandboxedTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir = mkdtemp()
        self.cwd = os.getcwd()
        os.chdir(self.tmpdir)

    def tearDown(self):
        os.chdir(self.cwd)
        rmtree(self.tmpdir)

    def assertFileTree(self, list_of_files):
        actual_file_list = sorted(walk_files())
        assert actual_file_list == sorted(list_of_files)
