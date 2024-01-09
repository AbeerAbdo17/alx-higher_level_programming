#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """method scop"""
    with open(filename, 'a', encoding='utf-8') as f:
        nbchar = f.write(text)
    return nbchar
