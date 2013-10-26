#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='Dwarf',
    version='0.1.0',
    author='Joeri Poesen',
    author_email='joeri@bantalabs.com',
    packages=['dwarf'],
    url='http://pypi.python.org/pypi/dwarf/',
    license='LICENSE',
    description='yet another static site generator',
    long_description=open('README.txt').read(),
    install_requires=[
        "Flask==0.10.1",
        "Jinja2==2.7.1",
        "Markdown==2.3.1",
        "MarkupSafe==0.18",
        "Werkzeug==0.9.4",
        "argparse==1.2.1",
        "itsdangerous==0.23",
        "wsgiref==0.1.2",
    ],


)
