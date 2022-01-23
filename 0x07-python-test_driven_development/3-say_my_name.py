#!/usr/bin/python3
"""This module have the function say_my_name
    Args:
        fisrt_name: string
        last_name: string
"""


def say_my_name(first_name, last_name=""):
    """print My name is <first name> <last name>"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
