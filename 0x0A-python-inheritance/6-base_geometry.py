#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """An instance of BaseGeometry class"""
    
    def __init__(self):
        """Creates an instance of BaseGeometry class"""
        pass

    def area(self):
        """Raises a not implemented Exception"""
        raise Exception("area() is not implemented")
