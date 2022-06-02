#!/usr/bin/python3
import sys
w = 0
for i in range(1, len(sys.argv)):
    j = int(sys.argv[i])
    w += j
if __name__ == '__main__':
    print(w)
