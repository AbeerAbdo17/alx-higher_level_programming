#!/usr/bin/python3

"""define class"""


class Square:
    """class scop"""
    def __init__(self, size=0, position=(0, 0)):
        """method scop"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """method scop"""
        return self.__position

    @position.setter
    def position(self, value):
        """method scop"""
        if not isinstance(value, tuple) \
                or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """method scop"""
        return self.__size ** 2

    def my_print(self):
        """method scop"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """method scop"""
        if self.__size != 0:
            [print("") for xv in range(0, self.__position[1])]
        for xv in range(0, self.__size):
            [print(" ", end="") for yv in range(0, self.__position[0])]
            [print("", end="#") for zv in range(0, self.__size)]
            if xv != self.__size - 1:
                print("")
        return ("")
