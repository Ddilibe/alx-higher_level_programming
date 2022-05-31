#!/usr/bin/python3
t = 0
for i in range(0, 9):
    t += 1
    for j in range(t, 10):
        if i == 8:
            print("{}{}".format(i, j))
            break
        print("{}{}, ".format(i, j), end="")
