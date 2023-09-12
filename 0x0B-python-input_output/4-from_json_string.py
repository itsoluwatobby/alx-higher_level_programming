#!/usr/bin/python3
"""Defines a function that returns an object (Python data
    structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """Return the object representation of a JSON string
    
    Args:
        my_str - string to represent
    """
    return json.loads(my_str)
