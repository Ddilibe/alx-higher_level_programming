#!/usr/bin/python3
def uniq_add(my_list=[]):
    q = 0
    for i in set(my_list):
        q += i
    return q
