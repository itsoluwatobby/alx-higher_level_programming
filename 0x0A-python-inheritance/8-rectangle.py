#!/usr/bin/python3
"""Defines a class Rectangel that inherits from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """An instance of Rectangle class"""
    
    def __init__(self, width, height):
        """Creates an instance of class Rectangle

        Args:
            width - given width of an instance of the Rectangle class
            height - given height of an instance of the Rectangle class
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
