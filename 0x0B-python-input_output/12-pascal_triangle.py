#!/usr/bin/python3
"""
    Module used to implement the paschal Triangle
"""


def pascal_triangle(n):
    """ Function that returns a list of integers representing the
    paschal's triangle of n"""
    new_list = []
    major_list = []
    if n >= 0:
        for i in range(n+1):
            for j in range(i+1):
                d = combination(i, j)
                new_list.append(int(d))
            major_list.append(new_list)
            new_list = []
    return (major_list)

def combination(x, y):
    """ Function used to implement combination in Mathematics """
    w = factorial(x - y)
    y = factorial(y)
    x = factorial(x)
    ans = (x) / (y * w)
    return (ans)

def factorial(x):
    """ Function used to implement factorial in Mathematics """
    if x == 1 or x == 0:
        return (1)
    return (x * factorial(x - 1))

