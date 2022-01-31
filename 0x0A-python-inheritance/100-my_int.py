#!/usr/bin/python3
"""This module have a class rebel"""


class MyInt(int):
    """Rebel class from int
    attribute of class value"""

    value = True

    def __eq__(self, other) -> bool:
        """Method to compare =="""
        value1 = self
        value2 = other
        if isinstance(other, int):
            MyInt.value = value1 != value2
        return MyInt.value

    def __ne__(self, other) -> bool:
        """Method to compare =="""
        return not MyInt.value
