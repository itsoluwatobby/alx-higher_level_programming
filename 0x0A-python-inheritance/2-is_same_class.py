#!/usr/bin/python3
"""A function that checks if an object is exactly an 
    instance of the specified class
"""

def is_same_class(obj, a_class):
    """Returns True if instance of obj is of class a_class
        else False

    Args:
        obj - given param to check its instance
        a_class - proposed class instance of obj
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
