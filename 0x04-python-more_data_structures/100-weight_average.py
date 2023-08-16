#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for tuppl in my_list:
        average += (tuppl[0] * tuppl[1])
        size += tuppl[1]
    return (average / size)
