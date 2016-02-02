#!/usr/bin/env python

from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()

PROJECT = u'ucrandomd'
VERSION = '1.0.0'
URL = 'https://github.com/SUNET/ucrandomd'
AUTHOR = u'Leif Johansson'
AUTHOR_EMAIL = u'leifj@sunet.se'
DESC = "Entropy distribution using unicast"

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=README,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='BSD',
    namespace_packages=[],
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-daemon',
    ],
    entry_points = {
        'console_scripts':
            ['ucrandomd=ucrandomd:main']
    },
    classifiers=[
    	# see http://pypi.python.org/pypi?:action=list_classifiers
        # -*- Classifiers -*- 
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        "Programming Language :: Python",
    ],
)
