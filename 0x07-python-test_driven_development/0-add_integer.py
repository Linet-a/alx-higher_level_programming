#!/usr/bin/python3
"""
0-add_ineterger module that supplies add_interger(a,b) function
adds two intergers a and b
"""


def add_integer(a, b=98):
    """Returns addition of two numbers"""
    if type(a) in (float, int):
        int(a)
    else:
        raise ValueError("a must be an interger")
    if type(b) in (float, int):
        int(b)
    else:
        raise ValueError("b must be an interger")
    return a + b
