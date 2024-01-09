#!/usr/bin/python3
"""module"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

fn = list(sys.argv[1:])

try:
    olddata = load_from_json_file("add_item.json")
except Exception:
    olddata = []

olddata.extend(fn)
save_to_json_file(olddata, "add_item.json")
