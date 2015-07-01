from __future__ import absolute_import

import ast

import click
from pathlib import Path

from more_itertools import unique_everseen


def walk_python_files(*paths):
    for path in paths:
        path = Path(path)
        if path.is_file() and path.suffix == '.py':
            yield str(path)
        elif path.is_dir():
            for f in walk_python_files(*path.iterdir()):
                yield f


def iter_imported_modules_from_file(python_file):
    with open(python_file, 'r') as f:
        source = f.read()
    tree = ast.parse(source, filename=python_file)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name_node in node.names:
                yield name_node.name
        elif isinstance(node, ast.ImportFrom):
            yield node.module


def iter_imported_modules(paths):
    for python_file in walk_python_files(*paths):
        for mod in filter(None, iter_imported_modules_from_file(python_file)):
            yield mod


@click.command()
@click.argument('paths', nargs=-1)
def cli(paths):
    """Lists all module names that are imported anywhere in the given paths"""
    for mod in sorted(unique_everseen(iter_imported_modules(paths))):
        print(mod)


if __name__ == '__main__':
    cli()
