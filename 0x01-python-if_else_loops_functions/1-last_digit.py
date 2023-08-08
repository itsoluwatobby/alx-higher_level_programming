#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strVal = str(number)
lastDigit = strVal[-1:]
print(f"Last digit of {number} is {lastDigit} and is", end=' ')
if int(lastDigit) > 5:
    print("greater than 5")
elif int(lastDigit) == 0:
    print("0")
elif int(lastDigit) > 0 and int(lastDigit) < 6:
    print("less than 6 and not 0")
