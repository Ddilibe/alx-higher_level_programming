#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}, ".format(i))
        break
    if i < 10:
        i = '0' + str(i)
    print("{}, ".format(i), end="")
