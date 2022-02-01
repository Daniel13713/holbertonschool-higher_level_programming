#!/usr/bin/python3
"""This module create an object from text file
with JSON representation"""


import json


def load_from_json_file(filename):
    """write with JSON representation
    JSON -> OBJECT_PYTHON (deserializing)"""

    with open(filename, mode="r", encoding="utf-8") as file:
        obj = json.load(file)
        return obj
