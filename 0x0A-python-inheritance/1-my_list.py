#!/usr/bin/python3
"""This module have a Class: Mylist
that inherist from list
"""


class MyList(list):
    """This class sorted the list
    arg:
        public method: print_sorted
    """

    def print_sorted(self):
        """Copy a list and print the copy sorted"""
        copy = self.copy()
        copy.sort()
        print(copy)
