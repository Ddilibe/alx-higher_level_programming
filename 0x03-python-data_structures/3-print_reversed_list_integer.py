#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 1
    while i < (len(my_list) + 1):
        print("{}".format(my_list[-i]))
        i += 1
