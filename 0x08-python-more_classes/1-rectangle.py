#!/usr/bin/python3
"""Defining my rectangle class"""


class Rectangle:
    """Rectangle class to represent rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize new Rectangle
        Args:
            width (int) -> Width of recangle instance
            height (int) -> Height of recangle instance
        """
        self.width = width
        self.height = height

    @property
    """Get width of rectangle"""
    def width(self):
        return self.__width

    @width.setter
    """Set width of recangle"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """Get height of rectangle"""
    def height(self):
        return self.__height

    @height.setter
    """Set height of rectangle"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
