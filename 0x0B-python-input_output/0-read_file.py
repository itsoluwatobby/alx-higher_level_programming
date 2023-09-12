#!/bin/usr/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename - file to read
    """
    with open('./my_file_0.txt') as fRead:
        print(fRead.read())
