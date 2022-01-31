#!/usr/bin/python3
"""This module have a class that inherits
from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Import BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Class rectangle
    arg: only init method"""

    def __init__(self, width, height):
        """Init method; width, height
        validation with integer_validator first"""

        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
