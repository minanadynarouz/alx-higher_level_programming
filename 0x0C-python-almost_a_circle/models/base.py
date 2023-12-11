#!/usr/bin/python3

"""Module base
Defines a Base class for other classes in the project
"""

import json
import os


class Base:
    """Base class
    Private class attribute: __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a Base instance
        Args:
        - id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        jsonFile = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        dicts_list = []
        with open(jsonFile, 'w') as f:
            for i in list_objs:
                dicts_list.append(i.to_dictionary())
            f.write(cls.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        """represent list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            newObj = cls(2, 3)
        elif cls.__name__ == "Square":
            newObj = cls(1)

        newObj.update(**dictionary)
        return newObj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        fileName = cls.__name__ + ".json"

        if not os.path.exists(fileName):
            return []
        with open(fileName, 'r') as f:
            listsObj = cls.from_json_string(f.read())
        list = []
        for dict in listsObj:
            list.append(cls.create(**dict))
        return list
