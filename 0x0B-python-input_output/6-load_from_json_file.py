#!/usr/bin/python3
"""Object creation from Json"""


import json


def load_from_json_file(filename):
    """create an Object from a Json file,
    Args:
        filename -> json file to get object from
    Return:
        new python ds object
    """
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
