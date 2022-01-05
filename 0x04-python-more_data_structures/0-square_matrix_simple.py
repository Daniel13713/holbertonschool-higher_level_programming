#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]
        return new_matrix
    return matrix
