#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """class square that define a square dimentions"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Gets value of size
        Args:
            none
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int) or not isinstance(value, float)):
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """Respond to =="""
        return self.area() == other.area()

    def __neq__(self, other):
        """Respond to !="""
        return self.area() != other.area()

    def __gt__(self, other):
        """Respond to >"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Respond to >="""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Respond to <"""
        return self.area() < other.area()

    def __le__(self, other):
        """Respond to <="""
        return self.area() <= other.area()
