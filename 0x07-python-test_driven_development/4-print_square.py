#!/usr/bin/python3
"""
    Module for the function prints a square
"""
def print_square(size):
    """ Function that prints a square"""
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
