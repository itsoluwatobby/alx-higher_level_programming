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
        """Returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
        if self.__size == 0:
            print("")
