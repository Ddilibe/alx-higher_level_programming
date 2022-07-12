#!/usr/bin/python3
"""
    Test Module for the Base class
"""


import unittest
from models.base import Base


class BassClass(unittest.TestCase):
    """
        Class for testing the base class
    """
    def test_for_increment(self):
        """ Method for testing for increment when assigned to different
        variables """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)

    def test_for_assignment(self):
        """ Method for testing for assigning value to the class """
        self.assertEqual(Base(55).id, 55)
        self.assertEqual(Base(98).id, 98)
        self.assertEqual(Base(22).id, 22)
        self.assertEqual(Base(249).id, 249)
