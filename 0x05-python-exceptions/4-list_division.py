#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    division = []
    for i in range(list_length):
        try:
            division.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            division.append(0)
        except (IndexError):
            print("out of range")
            division.append(0)
        except TypeError:
            print("wrong type")
            division.append(0)
    return division
