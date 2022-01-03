#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        max_number = sorted(my_list)[-1]
        return (max_number)
    return (None)
