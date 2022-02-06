#!/usr/bin/python3
"""
This module have the class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square
    Arg:
        - Private instances attributes:
            - width, height,, x, y with getter and setters
            (all initializate in super -> Rectnagle)
        Public method:
            -area
            -display
            - __str__
            - update
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter to size"""
        return getattr(self, "width")

    @size.setter
    def size(self, value):
        """setter to size"""
        setattr(self, "width", value)

    def __str__(self) -> str:
        return "[Square] ({0}) {1}/{2} - {3}".format(
            self.id, self.x, self.y, self.width
        )
