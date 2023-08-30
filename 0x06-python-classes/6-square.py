#!/usr/bin/python3

"""Definition of a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0,0)):
        """Initialize an instance of a square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position the new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the value of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the square
        Args: value (tuple): The position of the square. Defaults to (0, 0).
        Raise TypeError: If the value is not a tuple of 2 elements.
            or if the its first or second element is not an integer
            or is negative.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance
        (num, int) for num in value) or not all(num >= 0 for num in value)):
             raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current of area of the square"""

        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
