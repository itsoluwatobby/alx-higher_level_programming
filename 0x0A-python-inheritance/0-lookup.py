#!/usr/bin/python3
"""This a sis function that returns list of available attribute
   and methods of an object
"""


def lookup(obj):
    """Returns all attributes of an object"""
    return dir(obj)
