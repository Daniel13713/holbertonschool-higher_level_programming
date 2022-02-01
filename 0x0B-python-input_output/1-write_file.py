#!/usr/bin/python3
"""This module write and overwrite a string to a text file"""


def write_file(filename="", text=""):
    """Use UTF8 and with"""

    with open(filename, mode="w", encoding="utf-8") as file:
        writed_data = file.write(text)
        return (writed_data)
