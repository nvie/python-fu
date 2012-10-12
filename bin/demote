#!/usr/bin/env python
from __future__ import absolute_import

import sys
import os
import re
import argparse
from python_fu.module import Module


def parse_args():
    parser = argparse.ArgumentParser(
            description='Demotes Python packages to modules (if safe).')
    parser.add_argument('modules', nargs='+')
    return parser.parse_args()


def main():
    args = parse_args()

    modules = map(Module, args.modules)
    for module in modules:
        module.demote()


if __name__ == '__main__':
    main()
