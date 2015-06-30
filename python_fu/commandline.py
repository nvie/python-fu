import sys

import click


def info(msg):
    click.echo(msg)


def warning(msg):
    click.secho(msg, fg='yellow', file=sys.stderr)


def error(msg):
    click.secho(msg, fg='red', file=sys.stderr)


def exit(msg, exitcode=1):
    error(msg)
    sys.exit(exitcode)
