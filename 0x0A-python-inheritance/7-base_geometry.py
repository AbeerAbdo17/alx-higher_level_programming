#!/usr/bin/python3
"""Module"""


class BaseGeometry:
    """class scop"""
    def area(self):
        """method scop"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method scop"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
