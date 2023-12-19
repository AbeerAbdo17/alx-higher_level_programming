#!/usr/bin/python3
"""define class"""

import math


class MagicClass:
    """class scop"""
    def__init__(self, redius=0):
        """method scope"""
        self.__redius = 0
        if type(redius) is not int and type(redius) is not float:
            raise TypeError("rediusmust be a num")
        self.__redius = redius

    def area(self):
        """method scop"""
        return (self.__redius ** 2 * math.pi)

    def cir(self):
        return (2 * math.pi * self.__redius)
