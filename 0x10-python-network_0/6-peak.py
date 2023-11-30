#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    Find and returns  the peak value in a list

    Arguments:
        list_of_integer(list): An array of integers passed as an argument
    """
    if not len(list_of_integers):
        return None
    init = list_of_integers[0]
    for num in list_of_integers:
        if num > init:
            init = num
        else:
            pass
    return init
