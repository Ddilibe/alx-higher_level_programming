#!/usr/bin/python3
"""
    Module for testing validation in the Rectangle class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class ValidateAttribute(unittest.TestCase):
    """
        Class for testing the input validation for the rectangle class
    """
    def test_type_error(self):
        """ Method for testing the TypeError """
        self.assertRaises(TypeError, Rectangle, ("ee", 12))
        self.assertRaises(TypeError, Rectangle, (12, "34"))
        self.assertRaises(TypeError, Rectangle, (12, 23, "22"))
        self.assertRaises(TypeError, Rectangle, (12, 34, 56, "ee"))

    def test_value_error(self):
        """ Method for testing the Value error """
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 16, 29, -3)
        self.assertRaises(ValueError, Rectangle, 13, 82, 3, -4)
