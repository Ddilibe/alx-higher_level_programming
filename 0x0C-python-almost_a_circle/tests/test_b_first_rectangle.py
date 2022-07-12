#!/usr/bin/python3
"""
    Test Module for the Base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class FristRectangle(unittest.TestCase):
    """
        Class for testing the base class
    """
    def test_for_increment(self):
        """ Method for testing for increment when assigned to different
        variables """
        a = Rectangle(12, 20)
        b = Rectangle(12, 32, 45)
        c = Rectangle(12, 43, 45)
        d = Rectangle(33, 64)
        self.assertEqual(a.id, 5)
        self.assertEqual(b.id, 6)
        self.assertEqual(c.id, 7)
        self.assertEqual(d.id, 8)

    def test_for_assignment(self):
        """ Method for testing for assigning value to the class """
        self.assertEqual(Rectangle(12, 23, 34, 56, 55).id, 55)
        self.assertEqual(Rectangle(98, 45, 75, 34, 98).id, 98)
        self.assertEqual(Rectangle(22, 65, 75, 75, 22).id, 22)
        self.assertEqual(Rectangle(123, 2343, 66645, 34, 249).id, 249)

    def test_rectanglea(self):
        """ Method for testing rectangle A for the private attribute x"""
        rectanglea = Rectangle(23, 34)
        self.assertIs(rectanglea.x, 0)
        rectanglea.x = 3
        self.assertIs(rectanglea.x, 3)

    def test_rectangleb(self):
        """ Method for testing rectangle B for the private attribute Y """
        rectb = Rectangle(23, 54)
        self.assertIs(rectb.y, 0)
        rectb.y = 54
        self.assertIs(rectb.y, 54)
