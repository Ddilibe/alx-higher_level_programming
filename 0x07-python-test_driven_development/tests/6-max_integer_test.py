#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def testing_for_none(self):
        """ Texting for none in a list """
        self.assertIsNone(max_integer([]))

    def texting_for_max(self):
        """ Method for testing for max """
        self.assertEqual(max_integer([1,2,3,4]), 4)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
