#!/usr/bin/python3

"""Function that prints a user's name"""


def say_my_name(first_name, last_name=""):
    """Prints out a user's name
        
    Args:
        first_name: user's first name
        last_name: user's last name, defaulted to 
                   an empty string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
