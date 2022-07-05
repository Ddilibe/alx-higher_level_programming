#!/usr/bin/python3
"""
    A module that reads contents from a text file
"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
