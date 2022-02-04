#!/usr/bin/python3

###################################################################################
print("-----------------------------------[0-main ]------------------------------------")
###################################################################################
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)


"""
def add(*x):
    return sum(x)


def add_rev(*args):
    return sum(args)


print(add(1, 2, 3, 4))
a = [1, 2, 3, 4]
a0, *a12, a3 = a
print(add_rev(*a))
print(a0)
print(a12)
print(a3)
# merging lists
print(a12 + a == [*a12, *a])

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict_merged = {**dict1, **dict2}
# merging dictionaries
print(dict_merged)

string = "real python ilikeit"
a = [*string]
b = string.split(" ")
print(a)
print(b)
(*c,) = "stranger"
print(c)
"""
