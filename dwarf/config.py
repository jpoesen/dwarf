#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Config(object):
    DEBUG = False
    _basedir = os.path.abspath(os.path.dirname(__file__))

    # Make sure the app root folder contains a /content/ folder
    # (or a symlink to one), or change the value of CONTENT_PATH to 
    # whatever suits you.
    CONTENT_PATH = os.path.join(os.path.dirname(__file__)) + '/content/'

class ProductionConfig(Config):
    DEBUG = True
    TEMPLATE_PATH = 'templates/nova1'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(DevelopmentConfig):
    TESTING = True
