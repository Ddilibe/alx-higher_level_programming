#!/usr/bin/python3
import sys
w = 0
for i in range(1, len(sys.argv)):
    if '.' in str(sys.argv[i]):
        j = float(sys.argv[i])
    else:
        j = int(sys.argv[i])
    w += j
print(w)
