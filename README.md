python-fu: Useful shell scripts for Python devs
===============================================

[![Build status](https://travis-ci.org/nvie/python-fu.png)](https://travis-ci.org/nvie/python-fu)

Create dir structures for your modules easily:

    $ mkmodule foo.bar.qux
    $ tree foo
    foo
    ├── __init__.py
    └── bar
        ├── __init__.py
        └── qux.py

Easily promote module files:

    $ promote foo.bar.qux
    $ tree foo
    foo
    ├── __init__.py
    └── bar
        ├── __init__.py
        └── qux
            └── __init__.py

Easily demote modules files (if safe):

    $ demote foo.bar.qux
    $ tree foo
    foo
    ├── __init__.py
    └── bar
        ├── __init__.py
        └── qux.py

Safety first
============

These commands will never cause any data loss.


Installation
============

You can use `pip` to install python-fu:

```console
$ pip install python-fu
```
