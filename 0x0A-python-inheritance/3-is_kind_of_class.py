#!/usr/bin/python3
"""This module have a function that returns True
- if the object is an instance of,
-or if the object is an instance of a class
that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """Return true or false using isinstance"""
    if isinstance(obj, a_class):
        return True
    return False
