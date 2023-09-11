#!/usr/bin/python3
"""A function that checks if an object is an instance of, 
    or if the object is an instance of a class that 
    inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if instance of obj is of class a_class
        else False

    Args:
        obj - given param to check its instance
        a_class - proposed class instance of obj
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
