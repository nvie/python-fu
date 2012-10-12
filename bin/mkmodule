#!/usr/bin/env python
from __future__ import absolute_import

import sys
import os
import re
import argparse
from python_fu.module import Module
from python_fu.helpers import replace_extension
from python_fu.commandline import info, error, warning, exit


def parse_args():
    parser = argparse.ArgumentParser(
            description='Creates directory structures for Python packages.')
    parser.add_argument('--promote', '-p', action='store_true', default=False,
            help='Immediately promote the new module to a package.')
    parser.add_argument('modules', nargs='+')
    return parser.parse_args()


def main():
    args = parse_args()

    modules = map(Module, sorted(args.modules))
    for module in modules:
        if module.exists():
            warning('%s already exists, skipping.' % (module,))
            continue

        info('Creating %s' % (module.module_file,))
        module.create(args.promote)


if __name__ == '__main__':
    main()
