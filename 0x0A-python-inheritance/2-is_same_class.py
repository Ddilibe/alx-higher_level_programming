#!/usr/bin/python3
"""
    Module that declares whether an object
    is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Function that declares if an object is exactly an
    instance of a specified class
    """
    return (True if type(obj) == a_class else False)
