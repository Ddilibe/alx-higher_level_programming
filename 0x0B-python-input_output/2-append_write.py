#!/usr/bin/python3
"""
    Module for the function that appends a string at the end
    of a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file
    and returns the number of characters added """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
