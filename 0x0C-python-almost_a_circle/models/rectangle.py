#!/usr/bin/python3
"""module"""

from models.base import Base


class Rectangle(Base):
    """class scop"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method scop"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """method scop"""
        return self.__width

    @width.setter
    def width(self, value):
        """method scop"""
        self.validate_int("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """method scop"""
        return self.__height

    @height.setter
    def height(self, value):
        """method scop"""
        self.validate_int("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """method scop"""
        return self.__x

    @x.setter
    def x(self, value):
        """method scop"""
        self.validate_int("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """method scop"""
        return self.__y

    @y.setter
    def y(self, value):
        """method scop"""
        self.validate_int("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_int(self, attrbut_name, value):
        """method scop"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attrbut_name))

    def validate_positive(self, attrbut_name, value):
        """method scop"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attrbut_name))

    def validate_non_negative(self, attrbut_name, value):
        """method scop"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attrbut_name))

    def area(self):
        """method scop"""
        return self.__width * self.__height

    def display(self):
        """method scop"""
        for xv in range(self.__y):
            print()
        for yv in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """method scop"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """method scop"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for xv, arg in enumerate(args):
                setattr(self, attributes[xv], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method scop"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
