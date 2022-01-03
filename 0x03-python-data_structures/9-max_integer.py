#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        max_number = sorted(my_list)[-1]
        return (max_number)
    else:
        return (None)
