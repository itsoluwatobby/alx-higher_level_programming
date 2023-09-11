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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle class instance"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns a toString value of the rectangle class"""
        name = str(self.__class__.__name__)
        return ("[{}] {}/{}".format(name, self.__width, self.__height))
