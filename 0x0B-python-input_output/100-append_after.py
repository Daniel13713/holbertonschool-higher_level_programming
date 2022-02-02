#!/usr/bin/python3
"""This module append a text after a pattern"""


def append_after(filename="", search_string="", new_string=""):
    """insert after a ldeterminate line"""

    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines[i] += new_string
        f.writelines(lines)
