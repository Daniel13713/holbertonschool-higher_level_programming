#!/usr/bin/python3
"""This module try to add a new attribute"""


def add_attribute(obj, name, value):
    """Try to add new attribute"""
    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
