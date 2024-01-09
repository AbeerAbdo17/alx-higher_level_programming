#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """method scop"""
    with open(filename, 'w', encoding='utf-8') as f:
        nbchar = f.write(text)
    return nbchar
