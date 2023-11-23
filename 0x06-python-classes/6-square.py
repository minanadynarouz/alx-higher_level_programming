#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """class square that define a square dimentions"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets value of size
        Args:
            none
        Returns:
            size
        """
        return self.__size

    @property
    def position(self):
        """Gets value of size
        Args:
            none
        Returns:
            size
        """
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or type(value[0]) is not int or
                value[1] < 0 or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
