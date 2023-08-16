#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedKeys = sorted(a_dictionary)
    for key in sortedKeys:
        print("{}: {}".format(key, a_dictionary[key]))
