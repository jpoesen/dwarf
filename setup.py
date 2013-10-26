#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt")

# reqs is a list of requirement
# e.g. ["Flask==0.10.1","Jinja2==2.7.1","Markdown==2.3.1","MarkupSafe==0.18"]

reqs = [str(ir.req) for ir in install_reqs]

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
    install_requires=reqs,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],


)
