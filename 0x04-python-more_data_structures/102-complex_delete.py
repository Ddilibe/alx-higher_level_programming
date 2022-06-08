#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_for_delete = []
    for key, values in a_dictionary.items():
        if values == value:
            keys_for_delete.append(key)
    for i in keys_for_delete:
        del a_dictionary[i]
    return a_dictionary
