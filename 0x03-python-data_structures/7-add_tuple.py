#!/usr/bin/python3
def test(t=()):
    if len(t) == 0:
        t = (0, 0)
    elif len(t) == 1:
        t = (t[0], 0)
    return (t)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = test(tuple_a)
    tuple_b = test(tuple_b)
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]
    tuple_sum = (sum_1, sum_2)
    return (tuple_sum)
