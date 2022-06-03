#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b> \n1')
    else:
        a = int(sys.argv[1])
        s = sys.argv[2]
        b = int(sys.argv[3])
        if s not in ('+', '-', '*', '/'):
            print('Unknown operator. Avaliable operators: +, -, * and /\n1')
        else:
            if s == '+':
                print("{} + {} = {}\n0".format(a, b, add(a, b)))
            elif s == '-':
                print("{} - {} = {}\n0".format(a, b, sub(a, b)))
            elif s == '*':
                print("{} * {} = {}\n0".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}\n0".format(a, b, div(a, b)))
