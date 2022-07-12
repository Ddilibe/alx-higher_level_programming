#!/usr/bin/python3
"""
    Module for test the area method in the rectangle class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class AreaFirst(unittest.TestCase):
    """
        Class for testing the area method for the Rectange class
    """

    def test_rect_a(self):
        """ Method for testing the first rectangle area method"""
        recta = Rectangle(1, 3)
        self.assertEqual(recta.area(), 3)
        recta.x, recta.y = 12, 65
        self.assertEqual(recta.area(), 3)
        self.assertEqual(recta.x, 12)
        self.assertEqual(recta.y, 65)
        recta.width = 234
        recta.height = 2
        self.assertEqual(recta.area(), 468)

    def test_rect_b(self):
        """ Method for testing the second rectangle area method """
        rectb = Rectangle(9, 1)
        self.assertEqual(rectb.area(), 9)
        rectb.height = 20
        self.assertEqual(rectb.area(), 180)
        rectb.width = 20
        self.assertEqual(rectb.area(), 400)
