#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle without attributes
    Attirbutes:
        - getter, setter width(int)
        - getter and setter height(int)"""

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of width, show the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the height: change the value of the height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter of height, show the value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the width: change the value of the width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
