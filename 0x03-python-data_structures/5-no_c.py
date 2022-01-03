#!/usr/bin/python3
def no_c(my_string):
    string = ""
    string_ = [x for x in my_string if (x != 'c' and x != 'C')]
    return (string.join(string_))
