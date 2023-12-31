#!/usr/bin/python3

"""define class"""

import math


class MagicClass:
    """class scop"""
    def __init__(self, radius=0):
        """method scope"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """method scop"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """method scop"""
        return (2 * math.pi * self.__radius)
