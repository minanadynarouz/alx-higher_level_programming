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
        return super().area()

    def __str__(self):
        name = str(self.__class__.__name__)
        w = str(self.__width)
        h = str(self.__height)
        return f"[{name}] {w}/{h}"
