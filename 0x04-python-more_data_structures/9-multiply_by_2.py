#!/usr/bin/python3
# A function that returns a new dictionary
# with all values multiplied by 2
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for i in new_dictionary.values():
        i * 2
    for k, v in new_dictionary.items():
        return "{} : {}".format(k, v)
