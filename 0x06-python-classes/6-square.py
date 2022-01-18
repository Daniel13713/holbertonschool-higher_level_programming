#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that define a Square

    Attributes:
        - getter, setter size (int): return and change the value of the size
        - getter, setter position (tuple: (int, int))
        - area (int): calculate the area of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initilize a square
        Attributtes:
            - size (Private, int): size of the square
            - position (Private, tuple: (int, int)): coordinates of the square
        """
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

    @property
    def position(self):
        """int: return the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """change the value of position"""
        #: Position validations
        if (type(value[0]) != int or type(value[1]) != int) or (
            value[0] < 0
            or value[1] < 0
            or not isinstance(value, tuple)
            or len(value) != 2
        ):
            #: The positions should be integers
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Instance method
        Note:
            calculate the area of the square
        Returns:
            Area of the square
        """
        area = self.size * self.size
        return area

    def my_print(self):
        """that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        if position[0]>0 print position[1] spaces
        Return: Nothing
        """
        size = self.size
        onePosition = self.position[0]
        if size == 0:
            print("")
        else:
            for x in range(size):
                if onePosition > 0:
                    for y in range(onePosition):
                        print("", end=" ")
                for y in range(size):
                    print("{}".format("#"), end="")
                print("")
