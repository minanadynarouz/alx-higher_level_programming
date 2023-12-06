#!/usr/bin/python3

"""returns the dictionary description with simple data structure"""
import json



def class_to_json(obj):
    """Use __dict__ to get dict representation of object
    Args:
        obj -> is class
    Return: 
        Dict object representation
    """
    
    return obj.__dict__
