#!/usr/bin/python3
"""
     Module to a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """Function to multiply two matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    new_matrix = []
    w = 0
    value = 0
    cont = []
    for i in range(len(m_a)):
        if type(m_a[i]) != list:
            raise TypeError("m_a must be a list of lists")
        if type(m_b[i]) != list:
            raise TypeError("m_b must be a list of lists")
        if len(m_a[i]) == 0:
            raise ValueError("m_a can't be empty")
        if len(m_b[i]) == 0:
            raise ValueError("m_b can't be empty")
        while w < len(m_b[i]):
            for j in range(len(m_b)):
                if type(m_a[i][j]) != float and type(m_a[i][j]) != int:
                    raise ValueError("m_a should contain only integers or floats")
                if type(m_b[j][w]) != float and type(m_b[j][w]) != int:
                    raise ValueError("m_a should contain only integers or floats")
                value += m_a[i][j] * m_b[j][w]
            cont.append(value)
            value = 0
            w += 1
        new_matrix.append(cont)
        cont = []
        w = 0
    return new_matrix
