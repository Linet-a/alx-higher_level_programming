#!/usr/bin/python3

def no_c(my_string):
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            my_string.replace(ch, '')
        return my_string
