#!/usr/bin/python3

"""Function that prints a square with character #"""


def print_square(size):
    """Prints out a square with character #

    Args:
        size: length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            [print('#', end='') for i in range(size)]
            print()
