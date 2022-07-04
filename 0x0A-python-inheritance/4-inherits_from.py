#!/usr/bin/python3
"""
    Module that declares whether an object
    is an instance of a class it is directly
    or indirectly  inherited from
"""


def inherits_from(obj, a_class):
    """
    Function that declares if an object is inherited for
    (directly or indirectly) in a class
    """
    return (issubclass(type(obj), a_class))
