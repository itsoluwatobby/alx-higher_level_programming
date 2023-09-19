#!/usr/bin/python3
"""Defines a class Rectangle which inherits from the Base class"""

from models.base import Base


class Rectangle(Base):
    """Represents a class rectangle which inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intantiates a class Rectangle

        Args:
            width (int) - width of rectangle
            height (int) - height of rectangle
            x (int) - x side of rectangle
            y (int) - y side of rectangle
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.height = height
        self.__x = x
        self.y = y

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle with `#` character."""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
        *args (ints): New attribute values.
                - 1st arg represents id attribute
                - 2nd arg represents width attribute
                - 3rd arg represent height attribute
                - 4th arg represents x attribute
                - 5th arg represents y attribute
            **kwargs (dict): key/value pairs of attributes.
        """
            
        if args and len(args) != 0:
            m = 0
            for arg in args:
                if m == 0:
                    if arg is None:
                        self.__init__(self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = arg
                elif m == 1:
                    self.__width = arg
                elif m == 2:
                    self.__height = arg
                elif m == 3:
                    self.__x = arg
                elif m == 4:
                    self.__y = arg
                m += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
        }

    def __str__(self):
        """Returns the print() and str() representation of the Rectangle class."""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, self.id,
                                                       self.__x, self.__y,
                                                       self.__width, self.__height))                    
