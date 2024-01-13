#!/usr/bin/python3
"""module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class scop"""

    def __init__(self, size, x=0, y=0, id=None):
        """method scop"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """method scop"""
        return self.width

    @size.setter
    def size(self, value):
        """method scop"""
        self.width = value
        self.height = value

    def __str__(self):
        """method scop"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """method scop"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for xv, arg in enumerate(args):
                setattr(self, attributes[xv], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method scop"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
