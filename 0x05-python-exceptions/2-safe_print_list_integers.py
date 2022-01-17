#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num = x
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end="")
        except (ValueError, TypeError):
            num -= 1
            pass
        except (IndexError) as Error:
            print(Error)
    print("")
    return num
