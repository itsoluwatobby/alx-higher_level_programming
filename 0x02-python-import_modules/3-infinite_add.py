#!/usr/bin/python3

if __name__ == "__main__":
    """
        adds all the parsed command line
        arguments together
    """
    import sys

    num_args = sys.argv
    result = 0
    for index in range(len(num_args) - 1):
        result += int(num_args[index + 1])
    print("{}".format(result))
