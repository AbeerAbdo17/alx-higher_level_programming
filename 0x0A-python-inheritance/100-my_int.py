#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """class scop"""
    def __new__(cls, *args, **kwargs):
        """method scop"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """method scop"""
        return int(self) != other

    def __ne__(self, other):
        """method scop"""
        return int(self) == other
