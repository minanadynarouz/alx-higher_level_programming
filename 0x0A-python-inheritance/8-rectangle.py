#!/usr/bin/python3
"""Child Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents Rectangle and inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Constructor"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
