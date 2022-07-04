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
        super().__init__(size, size)
        self.__size = size
    
    def __str__(self):
        """ Method that describes a class """
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
