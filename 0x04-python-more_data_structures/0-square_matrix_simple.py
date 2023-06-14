#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared = [num ** 2 for num in row]
        squared_matrix.append(squared)
    return squared_matrix
