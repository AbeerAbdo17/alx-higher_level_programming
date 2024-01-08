#!/usr/bin/python3
"""Module"""


def add_attribute(obj, att, value):
    """method scop"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
