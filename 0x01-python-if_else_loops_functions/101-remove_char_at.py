#!/usr/bin/python3
def remove_char_at(str, n):
    t, f = 0, ""
    for i in str:
        if t != n:
            f += i
        t += 1
    return f
