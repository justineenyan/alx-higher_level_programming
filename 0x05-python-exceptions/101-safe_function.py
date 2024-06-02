#!/usr/bin/python3
from sys import stderr
# A function that executes a function safely.


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, IndexError, ValueError, TypeError) as e:
        stderr.write("Exception: {}\n".format(e))
        return None
