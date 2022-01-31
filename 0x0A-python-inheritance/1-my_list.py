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
        """Use sorted to sort the list"""
        print(sorted(self))
