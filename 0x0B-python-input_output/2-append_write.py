#!/usr/bin/python3
"""This module sppends a string to a text file"""


def append_write(filename="", text=""):
    """Use UTF8 and with"""

    with open(filename, mode="a+", encoding="utf-8") as file:
        writed_data = file.write(text)
        return (writed_data)
