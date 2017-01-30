#!/usr/bin/env python

from setuptools import setup

LONG_DESCRIPTION = open('README.rst').read()

setup(
    name='altslice',
    version='0.1.0',
    description='Alternative slicing and indexing',
    long_description=LONG_DESCRIPTION,
    author='Jonathan J. Helmus',
    author_email='jjhelmus@gmail.com',
    url='https://github.com/jjhelmus/altslice',
    license="BSD",
    py_modules=['altslice'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
     ]
)
