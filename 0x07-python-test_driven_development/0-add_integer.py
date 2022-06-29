#!/usr/bin/python3
"""
    Module to a function to a that adds 2 integers
"""


def add_integer(a, b=98):
    """Funtion that adds two integers
    Args:
        a: first Argument
        b: second argument assigned to 98
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
