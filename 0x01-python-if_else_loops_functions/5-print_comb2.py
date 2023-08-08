#!/usr/bin/python3
for num in range(0, 99):
    if num < 10:
        print("{}{}".format(0, num), end=', ')
    elif num >= 10:
        print(f"{num}", end=', ')
print(99)
