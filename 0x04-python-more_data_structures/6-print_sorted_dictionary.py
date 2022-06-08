#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dist = list()
    for k, l in a_dictionary.items():
        dist.append(k)
    dist.sort()
    for i in dist:
        print("{}: {}".format(i, a_dictionary.get(i)))
