#!/usr/bin/python3
"""This module have a class that inherits
from BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry
    arg:
        public method: area, integer_validator"""

    def area(self):
        """public method, calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value. Name is always str"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class rectangle
    arg: only init method"""

    def __init__(self, width, height):
        """Init method; width, height
        validation with integer_validator first"""

        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
