#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = my_list[0]
    if not my_list:
        return None
    for i in my_list:
        if i > my_list[0]:
            biggest = i
    return biggest
