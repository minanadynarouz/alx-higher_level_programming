#!/usr/bin/python3

"""JSON represntation from object"""


import json
def to_json_string(my_obj):
    """ Serialize object back to json form
    Args:
        my_obj -> Data to be returned to Json 
    Return:
         data in form of Json
    """
    return json.dumps(my_obj, separators=(', ', ': '))
