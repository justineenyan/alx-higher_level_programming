#!/usr/bin/python3
# A function that returns a key
# with the biggest integer value.
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v == maximum:
            return (f"{k}")
