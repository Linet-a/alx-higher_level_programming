#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print() #print new line after the integer
        return True
    except (ValueError, TypeError):
        return False

