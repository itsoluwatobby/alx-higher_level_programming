#!/usr/bin/python3

"""Definition a Square class."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize an instance of a square.

        Args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the area of the square"""

        return (self.__size * self.__size)
