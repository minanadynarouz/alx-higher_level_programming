#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """class square that define a square dimentions"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
