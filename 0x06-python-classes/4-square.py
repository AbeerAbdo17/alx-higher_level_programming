#!/usr/bin/python3

"""define class"""


class Square:
    """class scop"""
    def __init__(self, size=0):
        """method scop"""
        self.size = size

    @property
    def size(self):
        """method scop"""
        return self.__size

    @size.setter
    def size(self, value):
        """method scop"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method scop"""
        return self.__size ** 2
