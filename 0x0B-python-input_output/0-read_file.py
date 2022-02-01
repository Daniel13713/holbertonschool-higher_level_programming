#!/usr/bin/python3
"""This module read a teax file"""


def read_file(filename=""):
    """read a file with with and UTF8"""

    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
