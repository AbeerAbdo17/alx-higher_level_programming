#!/usr/bin/python3
"""no module"""


def read_file(filename=""):
    """method scop"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
