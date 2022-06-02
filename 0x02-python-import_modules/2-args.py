#!/usr/bin/python3
import sys
j = len(sys.argv) - 1
if __name__ == '__main__':
    if j == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif j > 0:
        print("{} arguments: ".format(j))
        for i in range(1,len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")

