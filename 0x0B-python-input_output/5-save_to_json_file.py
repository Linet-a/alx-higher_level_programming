#!/usr/bin/python3
"""
contains save_to_json_fie function
"""


import json


def save_to_json_file(my_obj, filename):
   """ writes an oject to a text file using json representation"""
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
