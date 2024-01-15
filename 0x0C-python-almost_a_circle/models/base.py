#!/usr/bin/python3
"""Module"""
import json
import csv


class Base:
    """class scop"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method scop"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method scop"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method scop"""
        file_name = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """method scop"""
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method scop"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """method scop"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                content = file.read()
                list_dicts = cls.from_json_string(content)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

