#!/usr/bin/python3
"""
Unittest for Class Rectangle
"""

from models.rectangle import Rectangle
import unittest


class TetsRectangleClass(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_first_rectangle(self):
        """Test for the fisrt rectangle writed"""

        r1 = Rectangle(10, 2)
        self.assertNotIsInstance(r1._Rectangle__height, Rectangle)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertNotIsInstance(r3.height, Rectangle)
