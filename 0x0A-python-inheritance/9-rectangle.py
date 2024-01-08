#!/usr/bin/python3
"""Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class scop"""
    def __init__(self, width, height):
        """method scop"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method scop"""
        return self.__width * self.__height

    def __str__(self):
        """method scop"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
