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
        k = ['first_name', 'age', 'last_name']
        if type(attrs) is list:
            args = {a: data[a] for a in attrs if type(a) is str and a in k}
            return args
        else:
            data_json = self.__dict__
            return data_json

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute"""

        if json:
            self.__dict__ = json
