#!/usr/bin/python3
def uppercase(str):
    res_str = ''
    for ch in str:
        if ch >= 97 and ch <= 122:
            res_str += chr(ord(ch) - 32)
        else:
            res_str += ch
    print('{}{}'.format(res_str), '\n')
