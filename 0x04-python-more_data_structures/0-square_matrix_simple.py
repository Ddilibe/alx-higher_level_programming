#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    e = len(matrix)
    matarix = list()
    for i in range(e):
        matarix.append(list(map(lambda x: x * x, matrix[i])))
    return matarix
