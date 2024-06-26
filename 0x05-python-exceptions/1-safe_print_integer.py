#!/usr/bin/python3
# A function that prints an integer with "{:d}".format().
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except ValueError as e:
        print("{} is not an integer".format(value))
        return False
