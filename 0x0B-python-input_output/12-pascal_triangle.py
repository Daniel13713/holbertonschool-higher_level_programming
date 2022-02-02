#!/usr/bin/python3
"""This module generate pascal's trinagle of n"""


def pascal_triangle(n):
    """Pascal's triangle of n"""
    triangle = []
    if n <= 0:
        triangle = []
    elif n == 1:
        triangle.append([1])
    elif n == 2:
        triangle.append([1])
        triangle.append([1, 1])
    else:
        triangle.append([1])
        triangle.append([1, 1])
        for i in range(2, n):
            triangle.append(
                [triangle[i-1][j-1] + triangle[i-1][j]
                    if j != 0 and i != j else 1 for j in range(0, i+1)]
            )
    return triangle
