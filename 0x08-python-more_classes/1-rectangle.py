#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """
        This is a class representation of Rectangle
    """

    def __init__(self, width=0, height=0):
        """
            This is an instance of the class Rectangle
            
            It takes in two parameter
        Args:
            width = The public Rectangle width
            height = The private Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the current width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets a new width for the Rectangle class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the current height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets a new height for the Rectangle class """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
