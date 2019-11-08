#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hiyapyco
import os
import sys

# load the yaml files
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(sys.argv[1]) as fp:
    yaml1 = fp.read()
with open(sys.argv[2]) as fp:
    yaml2 = fp.read()

merged_yaml = hiyapyco.load([yaml1, yaml2], method=hiyapyco.METHOD_MERGE)
out_file = open("/buildout/merged.yml", "w")
out_file.write(hiyapyco.dump(merged_yaml))
out_file.close()
