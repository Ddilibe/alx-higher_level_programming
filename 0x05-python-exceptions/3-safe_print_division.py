#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        w = a / b
    except:
        w = None
    finally:
        print("Inside result: {}".format(w))
    return (w)
