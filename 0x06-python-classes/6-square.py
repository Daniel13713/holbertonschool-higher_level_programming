#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that define a Square
    Attributes:
        - getter, setter size (int): return and change the value of the size
        - getter, setter position (tuple: (int, int))
        - area (int): calculate the area of the square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initilize a square"""
        self.size = size
        self.position = position

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
        """Instance method: calculate the area of the square"""
        area = self.size * self.size
        return area

    def my_print(self):
        """that prints in stdout the square with the character #:"""
        if self.size == 0:
            print("")
        else:
            for x in range(self.position[1]):
                print("")
            for y in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    @property
    def position(self):
        """int: return the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """change the value of position"""
        if type(value) != tuple or len(value) != 2\
           or type(value[0]) != int or type(value[1]) != int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
