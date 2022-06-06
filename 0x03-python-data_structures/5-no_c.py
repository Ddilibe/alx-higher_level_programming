#!/usr/bin/python3
def no_c(my_string):
    e = ""
    for i in my_string:
        if i in ['c', 'C']:
            continue
        e += i
    return e
