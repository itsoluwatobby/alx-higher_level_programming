#!/bin/usr/python3
"""Defines a function that writes a string to a text file
    and returns the number of character
"""


def write_file(filename="", text=""):
    """writes to a file and returns the number
        characters written

    Args:
        filename - file to write to
        text - content to write file
    """
    with open(filename, 'w', encoding="utf-8") as fWrite:
        return fWrite.write(text)
