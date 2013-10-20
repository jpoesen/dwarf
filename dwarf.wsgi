#!/usr/bin/python

activate_this = '/path/to/dwarf/virtual/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os, sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/path/to/dwarf")

from dwarf import app as application

if not application.debug:
    import logging
    this_dir = os.path.dirname(__file__)
    log_file = os.path.join(this_dir, 'dwarf_app.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    application.logger.addHandler(file_handler)
