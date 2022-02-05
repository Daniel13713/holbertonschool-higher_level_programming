#!/usr/bin/python3
"""
This module hav ethe class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle
    Arg:
        - Private instances attributes:
            - width, height,, x, y with getter and setters
        Public method:
            -area
            -display
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Setter to x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Setter to y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculate the are of the rectangle"""
        return self.height * self.width

    def display(self):
        """that prints in stdout the square with the character #:"""
        msg = "\n" * self.y
        for y in range(self.height):
            pos_x = " " * self.x
            msg += pos_x + "#" * self.width + "\n"
        print(msg, end="")
        return msg

    def __str__(self) -> str:
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(
            self.id, self.x, self.y, self.width, self.height
        )
