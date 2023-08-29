import math

"""Definition of a MagicClass matching a bytecode provided by Holberton"""

class MagicClass:
    """Represents a Circle"""
    __radius = None

    def __init__(self, value=0):
        """Initialize an instance MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

     def circumference(self):
        """Returns the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)

