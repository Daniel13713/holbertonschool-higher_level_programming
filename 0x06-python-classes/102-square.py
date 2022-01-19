#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that define a Square

    Attributes:
        - getter, setter size (int): return and change the value of the size
        - area (int): calculate the area of the square
    """

    def __init__(self, size=0):
        """Initilize a square
        Attributtes:
            - size (Private): size of the square

        First determinate if the value of the size is right,
         integer and positive
        """
        self.size = size

    def __eq__(self, other) -> bool:
        """Method to compare =="""
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """Method to compare =="""
        return self.area() != other.area()

    def __lt__(self, other):
        """Method to compare <"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Method to compare >"""
        return self.area() > other.area()

    def __le__(self, other):
        """Method to compare <="""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Method to compare >="""
        return self.area() >= other.area()

    @property
    def size(self):
        """int: return the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """change the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Instance method
        Note:
            calculate the area of the square
        Returns:
            Area of the square
        """
        area = self.size * self.size
        return area
