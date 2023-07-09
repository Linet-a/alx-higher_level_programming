#!/usr/bin/python3
"""4-print_square module tat supplies one function
print-square(size)
"""



def print_square(size):
    """prints square of a given size with character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an interger")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print("#" * size + "\n" * size, end="")
