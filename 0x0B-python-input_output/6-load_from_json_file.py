#!/usr/bin/python3
"""module"""
import json


def load_from_json_file(filename):
    """method scop"""
    with open(filename, 'r') as f:
        d = json.load(f)
    return d
