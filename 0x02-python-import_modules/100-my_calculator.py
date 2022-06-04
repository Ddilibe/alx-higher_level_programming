#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, div, mul
    import sys
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        s = sys.argv[2]
        b = int(sys.argv[3])
        if s not in ('+', '-', '*', '/'):
            print('Unknown operator. Avaliable operators: +, -, * and /')
            sys.exit(1)
        else:
            if s == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif s == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif s == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
