"""
python-fu: Python command line tools, for increased fu.
"""
import sys

from setuptools import find_packages, setup


def get_dependencies():
    dependencies = ['click >= 4.0', 'more_itertools']
    if sys.version_info < (3, 0):
        dependencies += ['pathlib']
    return dependencies

setup(
    name='python-fu',
    version='0.2',
    url='https://github.com/nvie/python-fu/',
    license='BSD',
    author='Vincent Driessen',
    author_email='vincent@3rdcloud.com',
    description=__doc__,
    packages=find_packages(),
    entry_points='''\
    [console_scripts]
    promote = python_fu.commands.promote:cli
    demote = python_fu.commands.demote:cli
    mkmodule = python_fu.commands.mkmodule:cli
    lsmodules = python_fu.commands.lsmodules:cli
    ''',
    # include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=get_dependencies(),
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.3',
        #'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
    ]
)
