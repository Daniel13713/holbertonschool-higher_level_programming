#!/usr/bin/python3
"""This module write an object to text file
using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """write with JSON representation
    OBJECT_PYTHON -> JSON (serializing)"""

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
