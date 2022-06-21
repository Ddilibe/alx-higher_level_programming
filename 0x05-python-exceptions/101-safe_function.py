#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        w = fct(*args)
    except (ZeroDivisionError, IndexError, TypeError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (None)
    return (w)
