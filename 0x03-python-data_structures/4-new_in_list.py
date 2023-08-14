#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list(my_list)
    if idx < 0:
        return (copy)
    if idx > len(my_list):
        return (copy)
    a = copy
    a[idx] = element
    return (a)
