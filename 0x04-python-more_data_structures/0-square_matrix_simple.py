#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [row[:] for row in matrix]
    result = "["
    for row in copy:
        result += "["
        for element in row:
            if element != row[-1]:
                result += "{:d}".format(element ** 2) + ", "
            else:
                result += "{:d}".format(element ** 2) + ""
        if row != copy[-1]:
            result += "], "
        else:
            result += "]]"
    return result
