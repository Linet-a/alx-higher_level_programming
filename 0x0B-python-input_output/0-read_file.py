#!/usr/bin/python3
def read_file(filename=""):
    """Reads text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
       print( f.read())
