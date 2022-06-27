#!/usr/bin/python3

"""
This module is composed by a class that defines a Rectangle
"""

class Rectangle:
    """ A rectangle class that defines a rectangle
        Public Class Attribute:
            number_of_inssances: recordes the number of instances
            print_symbol: Symbol for displaying the rectangle
        Private Instance Attribute:
            width: The width of the rectangle
            height: The height of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializing the class """
        if type(width) != int:
            raise TypeError('width must be an integer')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Method for returning the width """
        return (self.__width)

    @property
    def height(self):
        """ Method for returning the height """
        return (self.__height)

    @width.setter
    def width(self, value):
        """ Method for changing the width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Method for changing the value of the height """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Public instance method for the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Public instance methos that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Method that prints the rectangle with the character # """
        for i in range(self.__height):
            print(str(self.print_symbol) * self.__width)
        return ("")

    def __repr__(self):
        """ Method to return a string representation of the rectangle """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Method for deleting an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method that returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 > rect_2:
            return (rect_1)
        elif rect_2 > rect_1:
            return (rect_2)
        else:
            return(rect_1)

    def __gt__(self, other):
        """ Method for comparison of two instances """
        first = self.area()
        second = other.area()
        if first > second:
            return True
        else:
            return False

    @classmethod
    def square(cls, size=0):
        """ Method for declaring a rectangle to a square """
        return cls(size, size)
