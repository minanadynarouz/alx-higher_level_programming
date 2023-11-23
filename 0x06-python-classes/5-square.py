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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2


    def my_print(self):
        """Print square or empty line if value 0 """
        for i in range(0, self.__size):
            for x in range(0, self.__size):
                print("#", end="")
            print()

