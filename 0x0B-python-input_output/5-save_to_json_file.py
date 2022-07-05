#!/usr/bin/python3
"""
    Module of a function that writes an object to a text file
    Using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an objects to a text file using a
    JSON representation """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
    return 
