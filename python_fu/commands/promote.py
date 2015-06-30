from __future__ import absolute_import

import click
from python_fu.module import Module


@click.command()
@click.argument('modules', nargs=-1)
def cli(modules):
    """Promotes Python modules to packages"""
    for module in [Module(m) for m in modules]:
        module.promote()


if __name__ == '__main__':
    cli()
