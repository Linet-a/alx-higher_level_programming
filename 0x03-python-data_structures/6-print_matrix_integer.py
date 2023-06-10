#!/usr/bin/python3

vim def print_matrix_integer(matrix=[[]]):
    for elements in matrix:
        for i in elements:
            print('{:d}'.format(i), end=' ')
        print()
