#!/usr/bin/python3
def remove_char_at(str, n):
    str_remove = str
    if n >= 0:
        return str_remove[:n] + str_remove[n+1:]
    else:
        return str_remove
