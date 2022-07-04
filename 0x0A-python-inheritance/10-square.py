#!/usr/bin/python3
"""
    A module for defining a square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A square class defined using a square class
    """
    def __init__(self, size):
        """ Initializing the square class using a rectangle class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area"""
        return super().area()
