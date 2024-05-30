#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_items in matrix:
        for item in sub_items:
            if item is not sub_items[len(sub_items) - 1]:
                print("{:d}".format(item), end=" ")
            else:
                print("{:d}".format(item))
    print()
