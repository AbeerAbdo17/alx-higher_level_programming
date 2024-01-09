#!/usr/bin/python3
"""Module"""


class Student:
    """class scop"""

    def __init__(self, first_name, last_name, age):
        """method scop"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method scop"""i
        try:
            for attr in attrs:
                if attrs is None:
                    return self.__dict__
        except Exception:
            return self.__dict__
        x = dict()
        for k, v in self.__dict__.items():
            x[k] = v
        return x
