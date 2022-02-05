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

    def test_typeError(self):
        """Case Type error in the values Must be integers"""

        """Tests to TypeErrors"""
        typeErr = ["number", "10", 3.0, [1, 2], {"a": 1}, float("nan"), None]
        msgErrHeight = "height must be an integer"
        for err in typeErr:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(err, 10, "4")
            with self.assertRaisesRegex(TypeError, msgErrHeight):
                Rectangle(10, err, "4")
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(23, 10, err)
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(2, 10, 3, err)

    def test_valueError(self):
        """Tests to ValueErrors"""
        valueErr = [-2, -1024, -1]
        for err in valueErr:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(err, 10, 6)
            with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(10, err, 2)
            with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Rectangle(23, 10, err)
            with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                Rectangle(2, 10, 3, err)

        """Width and height must be > 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, 0, 6)
