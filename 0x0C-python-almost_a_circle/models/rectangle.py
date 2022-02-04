#!/usr/bin/python3
"""
This module hav ethe class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle
    Arg:
        - Private instances attributes:
            - width, height,, x, y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter to width"""
        return self.__width

    @property
    def height(self):
        """Getter to height"""
        return self.__height

    @property
    def x(self):
        """Getter to x"""
        return self.__x

    @property
    def y(self):
        """Getter to y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter to width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter to height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter to x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter to y"""
        self.__y = value
