#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
        Prevents user from instantiating new LockedClass attributes
        aside 'first_name'.
    """

    __slots__ = ["first_name"]
