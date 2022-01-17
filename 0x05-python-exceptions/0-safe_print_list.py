#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for num in range(x):
            print("{}".format(my_list[num]), end="")
        print("")
        if num > 0:
            num += 1
        return num
    except IndexError:
        print("")
        return num
