#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    keys, values = a_dictionary.keys(), a_dictionary.values()
    new_dic = dict(map(lambda key, value: (key, value * 2), keys, values))
    return new_dic
