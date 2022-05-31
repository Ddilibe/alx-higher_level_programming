#!/usr/bin/python3
def print_last_digit(number):
    if number != 0:
        if number < 0:
            k = -number % 10
        else:
            k = number % 10
    else:
        k = 0
    print("{}".format(k), end="")
    return k
