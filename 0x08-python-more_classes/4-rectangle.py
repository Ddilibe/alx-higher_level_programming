#!/usr/bin/python3

"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """A rectangle class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the class"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Method for returning the width"""
        return self.__width

    @property
    def height(self):
        """Method for returning the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Method for changing the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Method for changing the value of the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method for the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance methos that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Method that prints the rectangle with the character #"""
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """Method to return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
