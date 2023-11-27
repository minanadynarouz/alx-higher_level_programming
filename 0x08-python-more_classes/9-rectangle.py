#!/usr/bin/python3
"""Defining my rectangle class"""


class Rectangle:
    """Rectangle class with setters and getters"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int) ->  width of the rectangle.
            height (int)->  height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rectangle with the greater area.
        Args:
            rect_1 (Rectangle) -> Rectangle 1.
            rect_2 (Rectangle) -> Rectangle 2.
        Raises:
            TypeError: if any argument is not an object of the Rectangle class
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Rectangle with width and height equal to size.
        Args:
            size (int) -> width and height of the new rectangle
        """
        return (cls(size, size))

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Define a str to print the 'print_symbol' used"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect = rect + ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Define destructor print message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
