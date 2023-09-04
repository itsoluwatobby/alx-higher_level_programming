#!/usr/bin/python3

"""Function that prints a text with 2 new lines after 
    each of these characters
"""


def text_indentation(text):
    """Prints out a text with 2 new lines after each of these characters

    Args:
        text: string of text
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = 0
    while chars < len(text) and text[chars] == ' ':
        chars += 1

    while chars < len(text):
        print(text[chars], end="")
        if text[chars] == "\n" or text[chars] in ".?:":
            if text[chars] in ".?:":
                print("\n")
            chars += 1
            while chars < len(text) and text[chars] == ' ':
                chars += 1
            continue
        chars += 1
