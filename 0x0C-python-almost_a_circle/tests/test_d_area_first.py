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
    new_rectangle = Rectangle(12, 34, 56, 78, 90)

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

    def test_Z_with_dictionary(self):
        """ Method to test with a dictionary """
        old_rect = Rectangle(1, 2, 4, 5, 22)
        q = old_rect.to_dictionary()
        new_rect = Rectangle.create(**q)
        self.assertEqual(old_rect.id, new_rect.id)

    def test_for_first_update(self):
        """ Method to check for the firat update """
        self.new_rectangle.update(12)
        self.assertEqual(self.new_rectangle.id, 12)

    def test_for_second_update(self):
        """ Method to check for the second update """
        self.new_rectangle.update(12, 34)
        self.assertEqual(self.new_recctangle.id, 12)
        self.assertEqual(self.new_rectangle.width, 34)

    def test_for_second_update(self):
        """ Method to check for the second update """
        self.new_rectangle.update(12, 34, 56)
        self.assertEqual(self.new_rectangle.id, 12)
        self.assertEqual(self.new_rectangle.width, 34)
        self.assertEqual(self.new_rectangle.height, 56)
