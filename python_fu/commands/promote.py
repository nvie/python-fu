#!/usr/bin/env python
from __future__ import absolute_import

import argparse
from python_fu.module import Module


def parse_args():
    parser = argparse.ArgumentParser(
            description='Promotes Python modules to packages.')
    parser.add_argument('modules', nargs='+')
    return parser.parse_args()


def main():
    args = parse_args()

    modules = map(Module, args.modules)
    for module in modules:
        module.promote()


if __name__ == '__main__':
    main()
