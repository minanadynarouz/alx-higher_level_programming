#!/usr/bin/python3
"""Child Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents Rectangle and inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Constructor"""

        if self.integer_validator("Width", width):
            self.__width = width

        if self.integer_validator("Height", height):
            self.__height = height
