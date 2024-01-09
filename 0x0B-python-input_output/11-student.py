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
        """method scop"""
        try:
            for attr in attrs:
                if type(attrs) is str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        x = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                x[k] = v
        return x

    def reload_from_json(self, json):
        """method scop"""
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
