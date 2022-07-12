#!/usr/bin/python3
"""
    Test Module for the Base class
"""


import unittest
import csv
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BassClass(unittest.TestCase):
    """
        Class for testing the base class
    """
    def test_for_A_increment(self):
        """ Method for testing for increment when assigned to different
        variables """
        self.assertEqual(Base().id, 1)

    def test_for_B_second_increment(self):
        """ Method for testing the second increment """
        self.assertEqual(Base().id, 2)

    def test_for_C_third_increment(self):
        """ Method for testing the fourth increnment """
        self.assertEqual(Base().id, 3)

    def test_for_D_fourth_increment(self):
        """ Method for testing the fourth increment """
        self.assertEqual(Base().id, 4)

    def test_for_assignment(self):
        """ Method for testing for assigning value to the class """
        self.assertEqual(Base(55).id, 55)

    def test_for_second_assignment(self):
        """ Method for testing for second assignment value to the class """
        self.assertEqual(Base(98).id, 98)

    def test_for_third_assignment(self):
        """ Method for testing for second assignment value to the class """
        self.assertEqual(Base(22).id, 22)

    def test_for_fourth_assignment(self):
        """ Method for thesting for fourth assignment value to the class """
        self.assertEqual(Base(249).id, 249)

    def test_for_string(self):
        """ Method to test for string id """
        s = Base('23')
        self.assertEqual(s.id, '23')

    def test_for_float(self):
        """ Method to test for float of a variable """
        s = Base(123.5)
        self.assertEqual(s.id, 123.5)
