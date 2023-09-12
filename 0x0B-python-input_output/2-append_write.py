#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends to a file and returns the number
        characters adden

    Args:
        filename - file to append to
        text - content to write file
    """
    with open(filename, 'a', encoding="utf-8") as fAppend:
        return fAppend.write(text)
