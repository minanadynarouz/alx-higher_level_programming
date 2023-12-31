#!/usr/bin/python3
"""Module Rectangle that inherits from Base class
Defines a Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    Class describing rectangle
    __width -> width of the rectangle
    __height -> height of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width Attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width Attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height Attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height Attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x Attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x Attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y Attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y Attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines area of rectangle instance.
        Returns: area
        """
        return self.__width * self.__height

    def display(self):
        """Prints rectangle to stdout using #"""
        if self.__width <= 0 or self.__height <= 0:
            print()
            return

        symbol = "#"
        print("{}".format("\n" * self.__y), end="")
        for _ in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update instance attributes in corrospondance with *args
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError("id must be integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be integer")
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dict representation of a rectangle"""
        newDict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return newDict
