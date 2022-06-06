#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if type(i) == list:
            for h in i:
                print("{}".format(h), end=" ")
        print("\n")
