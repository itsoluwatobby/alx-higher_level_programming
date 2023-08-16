#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for ele in my_list:
        if ele == search:
            copy.append(replace)
        else:
            copy.append(ele)

    return (copy)
