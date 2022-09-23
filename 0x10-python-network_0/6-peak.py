#!/usr/bin/python3
""" Script aimed at training one for a technial interview"""
def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """
    long = len(list_of_integers)
    if long > 0:
        list_of_integers.sort()
        return list_of_integers[long-1]
    return None
