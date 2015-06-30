from __future__ import absolute_import

import click
from python_fu.module import Module


@click.command()
@click.option('--promote', '-p', flag=True,
              help='Immediately promote the new module to a package')
@click.argument('modules', nargs=-1)
def cli(modules, promote):
    """Creates directory structures for Python packages"""
    for module in [Module(m) for m in sorted(modules)]:
        if module.exists():
            warning('{} already exists, skipping.'.format(module))
            continue

        info('Creating {}'.format(module.module_file))
        module.create(promote)


if __name__ == '__main__':
    cli()
