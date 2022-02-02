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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved"""

        data = {
            'first_name': self.first_name,
            'age': self.age,
            'last_name': self.last_name
        }
        if type(attrs) is list:
            args = {
                arg: data[arg] for arg in attrs
                if type(arg) is str
                and arg in ['first_name', 'age', 'last_name']
            }
            return args
        else:
            data_json = self.__dict__
            return data_json
