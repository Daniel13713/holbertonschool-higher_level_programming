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
        if type(size) != int:  #: if not isintance(size, int)
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """int: return the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """change the value of size"""
        if type(value) != int:  #: if not isintance(size, int)
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
        area = self.__size * self.__size
        return area

    def my_print(self):
        """that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        Return: Nothing
        """
        size = self.__size
        if size == 0:
            print("")
        else:
            for x in range(size):
                for y in range(size):
                    print("{}".format("#"), end="")
                print("")
