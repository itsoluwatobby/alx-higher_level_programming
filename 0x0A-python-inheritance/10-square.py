#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents an instance of a Square class"""

    def __init__(self, size):
        """Initializes an instance of a Square class

        Args:
            size (int) - given size of an instance of the square class
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
