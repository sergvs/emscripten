#!/usr/bin/env python

raise Exception('emconfiguren is deprecated!')

'''
This is a helper script for emmaken.py. See docs in that file for more info.
'''

import os, sys

__rootpath__ = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
def path_from_root(*pathelems):
  return os.path.join(__rootpath__, *pathelems)
exec(open(path_from_root('tools', 'shared.py'), 'r').read())

Building.configure(sys.argv[1:])

