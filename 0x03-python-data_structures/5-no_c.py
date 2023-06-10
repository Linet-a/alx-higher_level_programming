#!/usr/bin/python3

def no_c(my_string):
    translation_table = {ord('c'): None, ord('C'): None}
    new_str = my_string.translate(translation_table)
    return new_str
