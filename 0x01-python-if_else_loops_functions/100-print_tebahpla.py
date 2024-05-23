#!/usr/bin/python3

for i in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 1:
        print(f"{chr(i).upper()}", end="")
    else:
        print(f"{chr(i)}", end="")
