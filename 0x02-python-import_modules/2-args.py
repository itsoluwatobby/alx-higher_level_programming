#!/usr/bin/python3

if __name__ == "__main__":
    """outputs parsed in arguments"""

    import sys

    args = sys.argv
    length = len(args) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {}".format(i + 1, args[i + 1]))
