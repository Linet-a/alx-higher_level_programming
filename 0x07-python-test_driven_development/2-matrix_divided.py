#!/usr/bin/python3
"""
module containing function mtrix_divide
"""


def matrix_divide(matrix, div):
    """divides matrix by div"""
    for sublist in matrix:
        for i in sublist:
            if not isinstance(i, int):
                raise TypeError("matrix must be a matrix (list of lists) o\
                        f integers/floats")
    first_len = len(matrix[0])
    for sublist in matrix:
        if len(sublist) != first_len:
            raise TypeError("Each row of the matrix must have the same siz\
                                                                        e")
    if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for sublist in matrix:
        new-sublist = [i / div for i in sublist]
        return round(new_matrix, 2)
        new-matrix.append(new_sublist)
