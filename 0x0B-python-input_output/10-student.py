#!/usr/bin/python3
"""Class Student"""


class Student:
    """Represent student"""
    def __init__(self, first_name, last_name, age):
        """Constructor - Initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a instance"""
        dict = self.__dict__
        if attrs is None:
            return self.__dict__

        newDict = {}
        for key in dict.keys():
            if key in attrs:
                newDict[key] = dict[key]
        return newDict
