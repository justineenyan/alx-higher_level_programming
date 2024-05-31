#!/usr/bin/python3
# A function that adds all unique integers in a
# List(only once for each integer)
def uniq_add(my_list=[]):
    new_result = set(my_list)
    Sum = 0
    for i in new_result:
        Sum += i
    return Sum
