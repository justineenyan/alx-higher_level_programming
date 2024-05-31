#!/usr/bin/python3
# A function that computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    result = []
    for row in new_matrix:
        new_row = [x * x for x in row]
        result.append(new_row)
    return result
