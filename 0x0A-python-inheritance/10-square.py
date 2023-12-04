#!/usr/bin/python3
"""Child Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents Square and inherits from Rectangle"""

    def __init__(self, size):
        """Constructor"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
