#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that define a Square"""

    def __init__(self, size=0):
        """Initilize a square
        Attributtes:
            - size (Private): size of the square

        First determinate if the value of the size is right,
         integer and positive
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Instance method
        Note:
            calculate the area of the square
        Returns:
            Area of the square
        """
        area = self.__size * self.__size
        return area
