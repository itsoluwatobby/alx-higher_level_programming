#!/usr/bin/python3
"""Defines a function that writes to a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj - object to write to file
        filename - file to write to
    """
    with open(filename, "w") as fWrite:
        json.dump(my_obj, fWrite)
