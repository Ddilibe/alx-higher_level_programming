#!/usr/bin/python3
"""
    A module that tests the str method of the rectangle class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class String(unittest.TestCase):
    """
    A class that test the str method of the rectangle class
    """
    q = "[Rectangle]"

    def string(self, soup):
        """ Function that displays some string with a class name """
        id, x, y, w, h = soup.id, soup.x, soup.y, soup.width, soup.height
        return " ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def test_first_rectangle(self):
        """ Method that tests the first rectangle """
        w = Rectangle(1, 3)
        w.x = 12
        w.y = 34
        w.id = 12
        ring = String.q + self.string(w)
        self.assertTrue(w)
