#!/usr/bin/python3
"""
    A modules that writes a string to a text file
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file and
    returns the number of charaters written """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
