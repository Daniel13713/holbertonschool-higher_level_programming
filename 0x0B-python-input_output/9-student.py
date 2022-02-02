#!/usr/bin/python3
"""This module have a class Student"""


class Student:
    """Class Student
    arg:
        -Public method:
        - attributes (public): first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        data_json = self.__dict__
        return data_json
