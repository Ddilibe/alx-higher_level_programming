#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        w = a_dictionary.pop(key)
    except KeyError:
        pass
    return a_dictionary
