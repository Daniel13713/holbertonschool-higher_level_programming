#!/usr/bin/python3
"""This module have a vacue class"""


class BaseGeometry:
    """empty class BaseGeometry
    arg:
        public method: area"""

    def area(self):
        """public method, calculate the area"""
        raise Exception("area() is not implemented")
