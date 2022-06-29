#!/usr/bin/python3
"""
    Module for a function that divides all elements f a matrix
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    args:
        @matrix: Lists of lists
        @div: The divisor argument
    """
    half = []
    whole = []
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (type(div) != float or type(div) != int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        w = matrix[i]
        if i == 0:
            one = len(w)
        if one != len(w):
            raise TypeError("Each row of the matrix must have the same size")
        for q in w:
            if not (type(q) != int or type(q) != float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            only = round(q / div, 2)
            half.append(only)
        whole.append(half)
        half = []
    return whole
