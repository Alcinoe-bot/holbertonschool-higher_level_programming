#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix):
        return ([[i * i for i in j] for j in matrix])
