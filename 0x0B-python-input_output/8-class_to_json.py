#!/usr/bin/python3
"""This module make a JSON serialization of an object"""


def class_to_json(obj):
    """return dict od the object"""
    data_json = obj.__dict__
    return data_json
