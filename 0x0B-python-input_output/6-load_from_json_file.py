#!/usr/bin/python3
"""Defines a function that reads from a text file"""
import json


def load_from_json_file(filename):
    """Creates an object from a text file

    Args:
        filename - file to load from
    """
    with open(filename) as fRead:
        return json.load(fRead)
