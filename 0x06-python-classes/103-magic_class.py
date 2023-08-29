import math

class MagicClass:
    __radius = None

    def __init__(self, radius=0):
        self.__radius = 0
        if type(value) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        return (self.__radius ** 2 * math.pi)
