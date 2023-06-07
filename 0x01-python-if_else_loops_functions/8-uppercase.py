#!/usr/bin/python3
def uppercase(str):
    res_str = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            res_str += chr(ord(ch) - 32)
        else:
            res_str += ch
    print('{}{}'.format(res_str), '\n')
