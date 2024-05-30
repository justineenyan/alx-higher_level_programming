#!/usr/bin/bash
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > int(len(my_list)):
        return None
    else:
        for i in my_list:
            if idx == i:
                return my_list[i]
