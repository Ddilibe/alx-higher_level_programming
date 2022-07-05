#!/usr/bin/python3
"""
    A module that creates an objects from a JSON file

"""


import json


def load_from_json_file(filename):
    """ Function that creates an object from a JSON file """
    with open(filename) as f:
        return (json.load(f))
