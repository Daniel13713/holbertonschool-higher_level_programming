#!/usr/bin/python3
"""This module have one function
is the object exactly an instance of the specified class?
"""


def is_same_class(obj, a_class):
    """Return True if the obj id exactly and
    instace of the a_class"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    return False
