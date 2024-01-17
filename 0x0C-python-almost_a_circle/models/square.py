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
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dict representation of a square"""
        newDict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return newDict
