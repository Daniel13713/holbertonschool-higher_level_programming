#!/usr/bin/python3
"""This module have the Mother class Base"""


class Base:
    """Class Base
    Arg:
        -class attribute
        -"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor with only id instance
        *you can assume that id is an integer
        """

        self.id = id

    @property
    def id(self):
        """getter if id"""
        return self._id

    @id.setter
    def id(self, value):
        """setter of the id"""
        if value is not None:
            self._id = value
        else:
            Base.__nb_objects += 1
            self._id = Base.__nb_objects
