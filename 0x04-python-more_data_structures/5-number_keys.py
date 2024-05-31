#!/usr/bin/python3
# A function that returns the number of keys in a dictionary.
def number_keys(a_dictionary):
    count = 0
    for i in a_dictionary.keys():
        count = count + 1
    return count
