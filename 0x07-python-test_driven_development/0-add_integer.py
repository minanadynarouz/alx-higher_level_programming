#!/usr/bin/python3
"""add integers together"""


def add_integer(a, b=98):
    """Function return the result of addition of a and b
    Args:
        a(int) -> The first arg, must be passed
        b(int) -> The second arg, if not passed, 98 is assumed to be the value
    Returns an int
    """
    try:
        if not (isinstance(a, int)) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        elif not (isinstance(b, int)) and not isinstance(b, float):
            raise TypeError("b must be an integer")

        return int(a) + int(b)
    except Exception as e:
        return (e)
