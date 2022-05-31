#!/usr/bin/python3
d = 0
f = 122
for i in range(26):
    if i % 2 == 1:
        p = f - 32
    else:
        p = f
    print("{}".format(chr(p)), end="")
    f -= 1
