#!/usr/bin/python3

def magic_calculation(a, b):
    """outputs the corresponding bytecode provided"""
    from magic_calculation_102 import add, sub

    if a < b:
        x = add(a, b)
        for i in range(4, 6):
            x = add(c, i)
        return (x)

    else:
        x = sub(a, b)
        return (x)
