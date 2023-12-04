#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        name = str(self.__class__.__name__)
        s1 = str(self.__size)
        s2 = str(self.__size)
        return f"[{name}] {s1}/{s2}"
