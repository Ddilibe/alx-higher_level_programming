#!/usr/bin/python3
"""
    Module for a function that returns the JSON
    representation of an object
"""

import json


def to_json_string(my_obj):
    """ Function that return the JSON representation og an object"""
    if json.dumps(my_obj):
        return (json.dumps(my_obj))
    return (my_obj)
