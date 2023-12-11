#!/usr/bin/python3
"""Module Square that inherits from Rectangle class
Defines a Square class
"""

from models.base import Base
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Class describing Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instanitating an object
        Attrs:
            size (int) -> size of the square
            x (int)    -> x-axis offset
            y (int)    -> y-axis offset
            id(int)    -> Unique identifier
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str() representation of an object"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update an instance's attributes"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation of a square"""
        newDict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return newDict
