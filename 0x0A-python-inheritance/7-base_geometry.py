#!/usr/bin/python3
"""Defines a class BaseGeometry"""

i
class BaseGeometry:
    """An instance of BaseGeometry class"""

    def area(self):
        """Raises a not implemented Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates a value and returns the resulting
            Exception if any

        Args:
            name - given string arg name
            value - expected to be an integer value
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
