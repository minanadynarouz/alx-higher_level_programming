#!/usr/bin/python3
"""Json Representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj -> object to switched to json then written to file
        filename -> json file to have the new data
    """
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            jsonData = json.dumps(my_obj, separators=(', ', ': '))
            f.write(jsonData)
