#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = -number % 10
    last = -last
else:
    last = number % 10
print("Last digit of {} is {} and is ".format(number,last), end="")
if last != 0:
    if last > 5:
        print("greater that 5")
    else:
        print("less that 6 and not 0")
else:
    print("0")
