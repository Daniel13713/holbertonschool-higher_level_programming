#!/usr/bin/python3
"""
This module have the class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square
    Arg:
    ----
        - Private instances attributes:
        -------------------------------
        size, x, y with getter and setters
        Public method:
        --------------
        area(width, height) -> int
        display(self) -> str
        __str__(self) -> str
        update(self, *args, **kwargs) -> Nothing
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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        attr = ["id", "size", "x", "y"]
        if len(args) != 0:
            for key, value in zip(attr, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation"""

        keys = ["id", "size", "x", "y"]
        values = [getattr(self, key) for key in keys]
        r_dict = dict(zip(keys, values))

        return r_dict
