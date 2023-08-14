#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    while length >= 0:
        length -= 1
        print("{:d}".format(my_list[length]))
        if length == 0:
            break
