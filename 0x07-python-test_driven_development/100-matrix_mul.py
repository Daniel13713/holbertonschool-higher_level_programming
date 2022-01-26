#!/usr/bin/python3
""""This module have a function that calculate the
multiplication of two matrices"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices"""
    # matrix must be a list
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # matrix must be a list of lists
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")

    # matrix can't be empty
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    # arguments must be integers or floats
    for i in m_a:
        for k in i:
            if type(k) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for k in i:
            if type(k) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    colums_a = len(m_a[0])
    rows_b = len(m_b)
    if colums_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")
    result = [
        [sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*m_b)]
        for X_row in m_a
    ]
    return result
