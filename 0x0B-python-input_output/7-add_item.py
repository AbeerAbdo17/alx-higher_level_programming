#!/usr/bin/python3
"""module"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

fn = list(sys.argv[1:])

try:
    olddata = load_from_json_file("add_item.json")
except Exception:
    olddata = []
olddata.extend(arglist)
save_to_json_file(olddata, "add_item.json")
