#!/usr/bin/python3

"""Definition a Square class."""

class Square:
    """Represent a square."""
    __size = None

    def __init__(self, size):
        """Initialize an instance of a square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

