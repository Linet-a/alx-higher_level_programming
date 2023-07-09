#!/usr/bin/python3
"""
0-add_ineterger module that supplies add_interger(a,b) function
adds two intergers a and b
"""


def add_integer(a, b=98):
    """Returns addition of two numbers"""
    if isinstance(a) in (float, int):
        a = int(a)
    else:
        raise TypeError("a must be an interger")
    if isinstance(b) in (float, int):
        b = int(b)
    else:
        raise TypeError("b must be an interger")
    return a + b
