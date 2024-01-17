#!/usr/bin/python3
"""Class Student"""


class Student:
    """Represent student"""
    def __init__(self, first_name, last_name, age):
        """Constructor - Initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of a instance"""
        return self.__dict__
