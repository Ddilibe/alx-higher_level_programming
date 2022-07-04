#!/usr/bin/python3
"""
    A module that practices inheritance on a builtin
    data type
"""


class MyList(list):
    """
        A class tha inherites the builtin data type list
    """
    def print_sorted(self):
        """ Method tha prints the list in acending order """
        w = self.copy()
        w.sort()
        print(w)
