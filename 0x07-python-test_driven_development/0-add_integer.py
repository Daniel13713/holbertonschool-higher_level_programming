#!/usr/bin/python3
""" This module add two integers or floats
    Use the add_integer(a, b) with a and b how integer or floats
    like: add_integer(1, 10)
    return: 11
"""


def add_integer(a, b=98):
    """Return the sum of a + b
    Args: a: integer or float
          b: integer or float"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
