#!/usr/bin/env python
#test
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['diagnostic_updater'],
    package_dir={'': 'src'}
)

setup(**d)
