#!/bin/usr/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename - file to read
    """
    with open(filename, encoding="utf-8") as fRead:
        print(fRead.read(), end="")
