#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    new_values = {key: value}
    a_dictionary.update(new_values)
    return a_dictionary
