#!/usr/bin/python3
"""A function that checks if an object that inherited 
    (directly or indirectly) from a specified class
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a_class the is
        inherited directed of indirectly else False
    Args:
        obj - given param to check its instance
        a_class - proposed class instance of obj
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
