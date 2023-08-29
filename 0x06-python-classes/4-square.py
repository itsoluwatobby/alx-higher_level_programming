#!/usr/bin/python3

"""Definition of a Square class"""
class Square:
    """Represents a square"""
    __size = None

    def __init__(self, size=0):
        """Initialize an instance of a square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size of  the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
