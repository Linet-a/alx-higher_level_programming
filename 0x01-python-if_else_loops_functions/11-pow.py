#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        result = 1 / pow(a, -b)
    elif b == 0:
        result = 1
    else:
        result = 1
        for _ in range(b):
            result *= a
    if a < 0 and b % 2 != 0:
        result = -result
    return result
