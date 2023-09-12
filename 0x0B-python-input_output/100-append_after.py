#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file, 
    after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): search string within the file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as fRead:
        for line in fRead:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fWrite:
        fWrite.write(text)
