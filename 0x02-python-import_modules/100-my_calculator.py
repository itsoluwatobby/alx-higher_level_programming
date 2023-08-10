#!/usr/bin/python3

if __name__ == "__main__":
    """outputs 10 math-function 5"""
    import sys
    from calculator_1 import add, div, sub, mul

    args = sys.argv
    if len(args) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if args[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    print("{} {} {} = {}".format(a, args[2], b, operators[args[2]](a, b)))
