#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary representation of a simple 
        data structure.

    Args:
        obj - given class object
    """
    return obj.__dict__
