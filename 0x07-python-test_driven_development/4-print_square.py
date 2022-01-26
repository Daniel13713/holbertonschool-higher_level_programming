#!/usr/bin/python3
"""This module print a square
    the size must be an integer
    the function return nothing
    try with print_square(1)
    obtain: #"""


def print_square(size):
    """that prints in stdout the square with the character #:
    Size must be an integer
    Return: nothing"""
    if type(size) != int or size != size:  #: if not isintance(size, int)
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print("")
    else:
        for y in range(size):
            print("#" * size)
