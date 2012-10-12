import sys


def info(msg):
    sys.stdout.write('%s\n' % (msg,))
    sys.stdout.flush()


def error(msg):
    sys.stderr.write('%s\n' % (msg,))
    sys.stderr.flush()


warning = error


def exit(msg, exitcode=1):
    error(msg)
    sys.exit(exitcode)
