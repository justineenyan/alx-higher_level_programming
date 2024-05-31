#!/usr/bin/python3
# Function that replaces all occurrences of an element
# By another in a new list.
def search_replace(my_list, search, replace):
    result = []
    new_list = my_list.copy()
    result = [replace if x == search else x for x in new_list]
    return result
