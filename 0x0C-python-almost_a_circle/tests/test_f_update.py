#!/usr/bin/python3
"""
    The Test module for the testing the update class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Update(unittest.TestCase):
    """
    Class for testing the update method added to the class
    """
    def test_first_rectangle(self):
        """ Method for testing the first rectangle class """
        recta = Rectangle(1, 2, 4, 5, 7)
        self.assertEqual(recta.id, 7)
        self.assertEqual(recta.width, 1)
        self.assertEqual(recta.x, 4)
        self.assertEqual(recta.height, 2)
        self.assertEqual(recta.y, 5)
        recta.update(59)
        self.assertEqual(recta.id, 59)

    def test_second_rectangle(self):
        """ Method for testing the second rectangle class """
        recta = Rectangle(1, 2, 4, 5, 7)
        self.assertEqual(recta.id, 7)
        self.assertEqual(recta.width, 1)
        self.assertEqual(recta.x, 4)
        self.assertEqual(recta.height, 2)
        self.assertEqual(recta.y, 5)
        recta.update(59, 34)
        self.assertEqual(recta.id, 59)
        self.assertEqual(recta.width, 34)

    def test_third_rectangle(self):
        """ Method for testing the third rectangle class """
        recta = Rectangle(1, 2, 4, 5, 7)
        self.assertEqual(recta.id, 7)
        self.assertEqual(recta.width, 1)
        self.assertEqual(recta.x, 4)
        self.assertEqual(recta.height, 2)
        self.assertEqual(recta.y, 5)
        recta.update(59, 34, 65)
        self.assertEqual(recta.id, 59)
        self.assertEqual(recta.width, 34)
        self.assertEqual(recta.height, 65)

    def test_fourth_rectangle(self):
        """ Method for testing the fourth rectangle class """
        recta = Rectangle(1, 2, 4, 5, 7)
        self.assertEqual(recta.id, 7)
        self.assertEqual(recta.width, 1)
        self.assertEqual(recta.x, 4)
        self.assertEqual(recta.height, 2)
        self.assertEqual(recta.y, 5)
        recta.update(59, 34, 65, 98)
        self.assertEqual(recta.id, 59)
        self.assertEqual(recta.width, 34)
        self.assertEqual(recta.height, 65)
        self.assertEqual(recta.x, 98)

    def test_fifth_rectangle(self):
        """ Method for testing a rectangle class for the fifth Rectangle """
        recta = Rectangle(1, 2, 4, 5, 7)
        self.assertEqual(recta.id, 7)
        self.assertEqual(recta.width, 1)
        self.assertEqual(recta.x, 4)
        self.assertEqual(recta.height, 2)
        self.assertEqual(recta.y, 5)
        recta.update(59, 34, 65, 98, 29)
        self.assertEqual(recta.id, 59)
        self.assertEqual(recta.width, 34)
        self.assertEqual(recta.height, 65)
        self.assertEqual(recta.x, 98)
        self.assertEqual(recta.y, 29)
