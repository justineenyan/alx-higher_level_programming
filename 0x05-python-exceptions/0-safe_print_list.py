#!/usr/bin/python3
# A function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            print("{}".format(my_list[count]), end="")
        except IndexError:
            break
        count += 1
    print("")
    return count
