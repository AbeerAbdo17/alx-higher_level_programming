#!/usr/bin/python3
"""Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class scop"""
    def __init__(self, size):
        """method scop"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method scop"""
        return self.__size ** 2
