#!/usr/bin/python3
"""Defines a class that inherits from the list object"""


class MyList(list):

    def print_sorted(self):
        """Prints a list in a sorted form"""
        print(sorted(self))
