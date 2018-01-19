# paths.py
#
# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Paths used throught this project.


from os.path import abspath, dirname, join


LOCAL_DIR = abspath(join(dirname(__file__), '..', '..'))
BASE_DIR = '/usr/share/kano-doc'

# When running this project from a local clone, adapt the base installation path.
if not LOCAL_DIR.startswith(BASE_DIR):
    BASE_DIR = LOCAL_DIR

RESOURCES_DIR = join(BASE_DIR, 'res')
DOCS_TEMPLATE_DIR = join(RESOURCES_DIR, 'docs-template')
