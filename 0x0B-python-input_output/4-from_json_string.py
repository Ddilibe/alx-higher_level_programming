#!/usr/bin/python3
"""
    A module that contains a function that returns an object
    (Python data structure) representaed by a JSON string
"""


import json


def from_json_string(my_str):
    """ Function that returns an boject (Python data structure)
    represented by a JSON string """
    return (json.loads(my_str))
