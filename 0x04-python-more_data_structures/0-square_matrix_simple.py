#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for item in row:
            squared_row.append(item ** 2)
        squared_matrix.append(squared_row)
    return squared_matrix
