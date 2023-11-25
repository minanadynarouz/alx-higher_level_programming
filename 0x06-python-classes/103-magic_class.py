#!/usr/bin/python3

"""Define a MagicClass matching a bytecode"""

import math


class MagicClass:
    """Represent a circle"""

    def __init__(self, radius=0):
        self.__radius = 0

        if (not isinstance(radius, int) or not isinstance(radius, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference"""
        return (2 * math.pi * self.__radius)

