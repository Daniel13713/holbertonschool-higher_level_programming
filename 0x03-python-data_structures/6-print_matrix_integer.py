#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            sep = " "
            for j in i:
                print("{:d}".format(j), end=sep)
                if i.index(j) + 2 == len(i):
                    sep = ""
            print("{}".format(""))
    return (0)
