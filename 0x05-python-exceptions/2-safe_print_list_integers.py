#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for elem in range(x):
            try:
                print("{:d}".format(my_list[elem]), end="")
            except (ValueError, TypeError):
                pass
            else:
                num += 1
        print("")
        return num

    except (IndexError) as Error:
        print(Error)
