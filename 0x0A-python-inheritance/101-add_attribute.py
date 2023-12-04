#!/usr/bin/python3
"""Func to add attribute if possible"""

def add_attribute(obj, name, value):
    """Add attribute to object"""
    
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
