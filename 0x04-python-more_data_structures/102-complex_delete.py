#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    copy = {}
    copy.update(a_dictionary)
    for key, value_own in a_dictionary.items():
        if value_own == value:
            copy.pop(key)
    a_dictionary.clear()
    a_dictionary.update(copy)
    return a_dictionary
