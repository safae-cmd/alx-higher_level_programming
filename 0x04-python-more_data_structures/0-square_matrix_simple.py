#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = matrix.copy()
    for i in range(len(matrix)):
        size[i] = list(map(lambda a: a**2, matrix[i]))
    return size
