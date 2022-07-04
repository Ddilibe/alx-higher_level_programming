#!/usr/bin/python3
"""
    A module that inherits a function from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A class that inherits the BaseGeometry class
    """
    def __init__(self, width, height):
        """ A class that initializes the rectangle class"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
