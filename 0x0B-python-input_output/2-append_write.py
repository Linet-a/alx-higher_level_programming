#!/usr/bin/python3
"""
contains append_write function
"""


def append_write(filename="", text=""):
    """returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
