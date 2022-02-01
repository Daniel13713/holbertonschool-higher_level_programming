#!/usr/bin/python3
"""This module return string representation"""


import json


def from_json_string(my_str):
    """string representation from JSON"""

    return json.loads(my_str)
