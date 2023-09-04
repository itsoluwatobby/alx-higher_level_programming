#!/usr/bin/python3

""" Defines a Rectangle class """

class Rectangle:
    """
        This is a class representation of Rectangle
    """

    def __init__(self, width=0, height=0):
        """
            This is an instance of the class Rectangle
            
            It takes in two parameter
        Args:
            width (int): The private Rectangle width
            height (int): The private Rectangle height
        """
        self.__width = width
        self.__height = height

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

    def area(self):
        """ 
            Returns the product of the width and the height 
            of the rectangle 
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            calculates the perimeter of a rectangle and 
            returns the resulting value
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """
            Instance method that returns an “informal” and nicely 
            printable string representation of an instance of the
            Rectangle class.

            Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        result = []
        for i in range(self.__height):
            [result.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                result.append("\n")
        return ("".join(result))

    def __repr__(self):
        """
            Instance method that returns an “official” string 
            representation of an instance of the Rectnagle class
        """
        rect_prop = "Rectangle(" + str(self.__width)
        rect_prop += ", " + str(self.__height) + ")"
        return (rect_prop)

    def __del__(self):
        """
            This instance method called when an instance of the 
            Rectangle class is deleted
        """
        print("Bye rectangle...")
