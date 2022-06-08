#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) != dict:
        return None
    values = list(a_dictionary.values())
    first = values[0]
    for i in values:
        if i > first:
            first = i
    for i, j in a_dictionary.items():
        if j == first:
            return i
