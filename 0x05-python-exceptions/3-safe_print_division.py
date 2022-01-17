#!/usr/bin/python3


def safe_print_division(a, b):
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        return None
    else:
        return division
    finally:
        print("inside result: {}".format(division))
