#!/usr/bin/python3
"""Lookup for attributes and methods of an object """


def lookup(obj):
    """Function to return all attributes and method of
    an object
    Args:
        obj(object of any class) -> The object in question
    Returns:
        list
    """

    return dir(obj)
