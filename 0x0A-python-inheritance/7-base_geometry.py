#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """An instance of BaseGeometry class"""
    
    def __init__(self):
        """Creates an instance of BaseGeometry class"""
        pass

    def area(self):
        """Raises a not implemented Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates a value and returns the resulting
            Exception if any

        Args:
            name - given string arg name
            value - expected to be an integer value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
