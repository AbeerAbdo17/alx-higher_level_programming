#!/usr/bin/python3
""" class"""


class Rectangle:
    """class scop"""
    def __init__(self, width=0, height=0):
        """ method scop"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method scop"""
        return self.__width

    @width.setter
    def width(self, value):
        """method scop"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method scop"""
        return self.__height

    @height.setter
    def height(self, value):
        """method scop"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method scop"""
        return self.__width * self.__height

    def perimeter(self):
        """method scop"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """method scop"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
