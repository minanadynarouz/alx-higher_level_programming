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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        name = str(self.__class__.__name__)
        w = str(self.__width)
        h = str(self.__height)
        return f"[{name}] {w}/{h}"
