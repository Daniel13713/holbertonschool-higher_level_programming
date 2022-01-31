#!/usr/bin/python3
"""This module have a two classes BaseGeometry
and Rectangle that inherist from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle
    arg: init method, area and str"""

    def __init__(self, width, height):
        """Init method; width, height
        validation with integer_validator first"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Publuc methos, calculate the area"""
        return self.__height * self.__width

    def __str__(self) -> str:
        """str method, string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
