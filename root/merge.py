#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hiyapyco
import jinja2
import os
import sys
import yaml

# load the yaml files
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(sys.argv[1]) as fp:
    yaml1 = fp.read()
with open(sys.argv[2]) as fp:
    yaml2 = fp.read()

# run jinja rendering
template = jinja2.Environment(loader=jinja2.BaseLoader()).from_string(yaml2)
yaml2 = template.render(version=os.getenv('VERSION'))

## delete entry in main yaml ##
# load the yaml into dict
main = yaml.safe_load(yaml1)
mod = yaml.safe_load(yaml2)
# grab the names of the first 2 depth keys
for key, value in mod.items() :
    dict1 = key
for key, value in mod[dict1].items() :
    dict2 = key
# delete the specific keyname from the source yaml
del main[dict1][dict2]
yaml1 = yaml.dump(main)

# merge the yaml files
merged_yaml = hiyapyco.load([yaml1, yaml2], method=hiyapyco.METHOD_MERGE)
# sort yaml
sortedl = yaml.safe_load(hiyapyco.dump(merged_yaml))
sortedyaml = yaml.dump(sortedl)
out_file = open("/buildout/merged.yml", "w")
out_file.write(sortedyaml)
out_file.close()
