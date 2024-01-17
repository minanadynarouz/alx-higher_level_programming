#!/usr/bin/python3
""" Check instance of class"""


def is_same_class(obj, a_class):
    """Function to check instance of class
    Args:
        obj -> objecct to check if instance of class
        a_class -> class to compare it with
    Return:
        True if obj is instance
        False if obj is not
    """
    return isinstance(obj, a_class) and type(obj) == a_class
