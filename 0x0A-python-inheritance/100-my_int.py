#!/usr/bin/python3
"""
    Testing and declearing a new class
"""


class MyInt:
    """
        Defining a class
    """
    def __init__(self, pl=0):
        """ Initializing the class with pl """
        self.pl = pl

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        if type(other) == int:
            return not self.pl == other
        return not self.pl == other.pl

    def __ne__(self, other):
        """Return True if vector differs from other."""
        if type(other) == int:
            return self.pl == other
        return self.pl == other.pl

    def __str__(self):
        """ Method for describing a class """
        return str(self.pl)
