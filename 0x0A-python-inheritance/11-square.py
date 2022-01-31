#!/usr/bin/python3
"""This module create a class Square
inherits from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class, define size"""

    def __init__(self, size):
        """define size
        with super().__init__ define a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate area of the square"""
        return self.__size ** 2

    def __str__(self) -> str:
        """string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
