#!/usr/bin/python3
def element_at(my_list, idx):
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
