#!/usr/bin/python3
"""
    Module containing a function that adds new attribute to
    an oject if it is possible
"""


def add_attribute(mc, name, first_name):
    """ Function that adds a new attribute to an object if possible """
    cards = [list, set, str, int, float, tuple]
    if type(mc) not in cards:
        mc.name = first_name
    else:
        raise TypeError('can\'t add new attribute')
