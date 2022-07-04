#!/usr/bin/python3
"""
    Module for a class
"""


class BaseGeometry:
    """
    A class without an  initialization
    """
    def area(self):
        """ A function that rasies an exception message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Function that validates the input value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
