#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[0] if len(tuple_a) > 0 else 0
    y = tuple_a[1] if len(tuple_a) > 1 else 0
    f = tuple_b[0] if len(tuple_b) > 0 else 0
    z = tuple_b[1] if len(tuple_b) > 1 else 0
    return (x + f, y + z)
