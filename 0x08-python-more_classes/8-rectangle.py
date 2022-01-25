#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle without attributes
    Attirbutes:
        - getter, setter width(int)
        - getter and setter height(int)
        - publics methos area and perimeter
        - str method: string representation
        - repr method: return string representation objetc
        - del: print message
        - public instance of the class: number_of_instances
        - public instance of the object: print_symbol"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Public instance method: calculate the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Public method that calculate the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """method that return a string representation to user"""
        msg = ""
        if self.width == 0 or self.height == 0:
            msg = ""
        else:
            for i in range(self.height):
                msg += str(self.print_symbol) * self.width
                if i != self.height - 1:
                    msg += "\n"
        return msg

    def __repr__(self) -> str:
        """Method that return a string representation
        to be able to recreate a new instance by using eval()
        to the developer"""
        msg = "Rectangle({0}, {1})".format(self.width, self.height)
        return msg

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
