#!/usr/bin/python3


def weight_average(my_list=[]):
    result = 0
    if my_list is not None:
        suma = list(map(lambda x: x[0] * x[1], my_list))
        total = [x[1] for x in my_list]
        if total != 0:
            result = sum(suma) / sum(total)
    return result
