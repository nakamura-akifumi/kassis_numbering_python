#!/usr/bin/env python

from setuptools import setup, find_packages

import os
import sys
import version

libdir = "kassis_numbering_python"
bindir = os.path.join(libdir, "bin")

sys.path.insert(0, libdir)

setup(
    name        = 'kassis_numbering',
    version     = version.VERSION,
    packages    = find_packages(),
    install_requires = open('requirements.txt').read().splitlines(),
    description = 'Python client for Kassis Numbering',
    zip_safe    = True,
    options     = {'easy_install': {'allow_hosts': 'pypi.python.org'}},
    include_package_data = False,
    license     = 'MIT License',
    platforms   = 'Platform Independent',
    author      = 'Akifumi NAKAMURA',
    author_email='tmpz84@gmail.com',
    url         = 'https://github.com/nakamura-akifumi/kassis_numbering_python',
    classifiers = ['License :: OSI Approved :: MIT License',
                  'Intended Audience :: Developers',
                  'Operating System :: OS Independent',
                  'Programming Language :: Python :: 3.3',
                  'Programming Language :: Python :: 3.4',
                  'Topic :: Database']
)
