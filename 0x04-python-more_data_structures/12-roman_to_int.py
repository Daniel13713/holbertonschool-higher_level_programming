#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
        decimal_list = list(map(lambda x: values[x], roman_string))
        decimal_list.reverse()
        result = decimal_list[0]
        for i in range(1, len(decimal_list)):
            if decimal_list[i] < decimal_list[i - 1]:
                result -= decimal_list[i]
            else:
                result += decimal_list[i]
        return abs(result)
    else:
        return 0
