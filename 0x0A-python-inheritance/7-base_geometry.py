#!/usr/bin/python3
"""Class represent Geometry"""


class BaseGeometry:
    """BaseGeometry as the base class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        try:
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            elif value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        except Exception as ex:
            return ex
