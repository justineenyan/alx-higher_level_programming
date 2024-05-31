#!/usr/bin/python3
# A function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("The dictionary is None.")
        return
    if not isinstance(a_dictionary, dict):
        print("The input is not a dictionary.")
        return
    [print("{} : {}".format(k, v)) for k, v in (sorted(a_dictionary.items()))]
