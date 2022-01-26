#!/usr/bin/python3
"""This module divide all element of the matrix
    use matrix_divided(matrix, div)
    with div like integer or float
    All elements of the matrix must be integers or floats
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all element divided by div
    rounded to 2 decimal places
    elements of matrix and div must be integer or floats"""
    msg0 = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or type(matrix[0]) != list:
        raise TypeError(msg0)
    for i in matrix:
        if type(i) != list or len(i) == 0:
            raise TypeError(msg0)
        for j in i:
            if type(j) not in [int, float] or j != j:
                raise TypeError(msg0)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[float("{:0.2f}".format(x / div)) for x in row] for row in matrix]
