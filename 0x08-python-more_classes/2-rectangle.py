#!/usr/bin/python3
"""Defining my rectangle class"""


class Rectangle:
    """Rectangle class with setters and getters"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int) ->  width of the rectangle.
            height (int)->  height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
