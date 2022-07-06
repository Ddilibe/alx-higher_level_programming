#!/usr/bin/python3
"""
    Module for a file that uses two different
    JSON function form different files
"""


import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
try:
    inside = load_from_json_file("add_item.json")
except Exception as e:
    inside = []

for i in range(1, len(sys.argv)):
    inside.append(sys.argv[i])

outside = save_to_json_file(inside, "add_item.json")
