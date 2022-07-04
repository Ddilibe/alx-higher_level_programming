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
        if type(value) == int:
            if value <= 0:
                card = str(name) + " must be greater than 0"
                raise ValueError(card)
            else:
                return (True)
        else:
            card = str(name) + " must be an integer"
            raise TypeError(card)
