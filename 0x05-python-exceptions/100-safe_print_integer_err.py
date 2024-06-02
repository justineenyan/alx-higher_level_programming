#!/usr/bin/python3
from sys import stderr
# A function that prints an integer.
def safe_print_integer_err(value):
        try:
            print("{:d}".format(value))
            return True
        except (TypeError,ValueError) as e:
            stderr.write("Exception: {}\n".format(e))
            return False
