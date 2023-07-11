#!/usr/bin/python3
"""
contains from_json_string function
"""


import json


def from_json_string(my_str):
    """rturns an object represented by a json string"""
    return json.loads(my_str)
