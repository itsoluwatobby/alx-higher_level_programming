#!/usr/bin/python3
"""
Defines a class Square that inherits for the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates the sqaure class
    
        Args:
            Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The id of the new Square.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """
        Update the Square.

        Args:
        *args (ints): New attribute values.
                - 1st arg represents id attribute
                - 2nd arg represent size attribute
                - 3rd arg represents x attribute
                - 4th arg represents y attribute
            **kwargs (dict): key/value pairs of attributes.
        """

        if args and len(args) != 0:
            m = 0
            for arg in args:
                if m == 0:
                    if arg is None:
                        self.__init__(self.__size, self.x, self.y)
                    else:
                        self.id = arg
                elif m == 1:
                    self.__size = arg
                elif m == 2:
                    self.__x = arg
                elif m == 3:
                    self.__y = arg
                m += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.__size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.__size = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.
        """
        return {
            "id": self.id,
            "x": self.x,
            'size': self.__size,
            "y": self.y
        }

    def __str__(self):
        """
        Returns the print() and str() representation of the Square class.
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                                       self.x, self.y,
                                                       self.__size))
