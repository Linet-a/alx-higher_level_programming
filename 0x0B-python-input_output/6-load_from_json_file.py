#!/usr/bin/python3
"""
loads from json file
"""

import json


def load_from_json_file(filename):
    """creates an obect from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
