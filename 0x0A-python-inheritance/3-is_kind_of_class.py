#!/usr/bin/python3
"""
    Module that declares whether an object
    is an instance of a class or of a subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Function that declares if an object is exactly an
    instance of a specified class
    """
    return (isinstance(obj, a_class))
