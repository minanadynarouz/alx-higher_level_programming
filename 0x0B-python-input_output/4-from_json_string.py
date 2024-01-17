#!/usr/bin/python3

"""JSON represntation from object"""


import json


def from_json_string(my_str):
    """ Serialize object back to python ds form
    Args:
        my_str -> Data to be returned to python ds
    Return:
         data in form of python ds
    """
    return json.loads(my_str)
