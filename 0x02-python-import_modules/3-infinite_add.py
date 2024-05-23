#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    argv = sys.argv[1:]

    for arg in argv:
        num = int(arg)
        result += num
        print("{:d}".format(result))
