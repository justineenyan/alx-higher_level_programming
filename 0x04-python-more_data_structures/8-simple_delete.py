#!/usr/bin/python3
# A function that deletes a key in a dictionary.
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        if key in a_dictionary:
            del a_dictionary[key]
            return a_dictionary