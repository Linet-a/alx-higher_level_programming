#!/usr/bin/python3
"""
contains write file function
"""


def write_file(filename="", text=""):
    """
    writes a string to text file(utf8)
    returns the characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
