#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    length = len(argv)
    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{length} arguments:")
        for index in range(length):
            print(f"{index + 1}: {argv[index]}")
