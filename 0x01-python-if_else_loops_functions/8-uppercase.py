#!/usr/bin/python3
def uppercase(str):
    e = 0
    for i in str:
        if 97 <= ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
        e  += 1
    print("")
    return e
