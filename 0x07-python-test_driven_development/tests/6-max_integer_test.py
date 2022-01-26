#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
from cmath import nan
import unittest

from numpy import NaN

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for the function"""

    def test_positive_numbers(self):
        """Test positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([100, 2123, 3123, 4123]), 4123)
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16]), 16)
        self.assertEqual(max_integer([2]), 2)

    def test_negative_numbers(self):
        """test negative numbers"""
        self.assertEqual(max_integer([-10, -5, 5, 10]), 10)
        self.assertEqual(max_integer([-1024, -23, -345, -23]), -23)

    def test_float_number(self):
        """Test float numbers"""
        self.assertEqual(max_integer([-0.5, -2.3, 4.5, -9.3]), 4.5)
        self.assertEqual(max_integer([-0.5]), -0.5)

    def test_vacue_list(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_list_of_something(self):
        """Test of list of something, not only integers"""
        self.assertEqual(max_integer([[1, 2]]), [1, 2])
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        self.assertEqual(max_integer([(-5, 100.2), (-5, 100.4)]), (-5, 100.4))
        self.assertEqual(max_integer([{"one": 1}]), {"one": 1})
        self.assertEqual(max_integer(["ah", "azz", "az"]), "azz")
        self.assertEqual(max_integer(["zaa", "azz", "az"]), "zaa")
        self.assertEqual(max_integer([[]]), [])
        self.assertEqual(max_integer([[], []]), [])
        self.assertEqual(max_integer([[True], [False]]), [True])

    def test_tuples(self):
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer((-10, -2, -1, -3, -4)), -1)
        self.assertEqual(max_integer(()), None)

    def test_strings(self):
        self.assertEqual(max_integer("hola"), "o")
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
