#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
#if you want to see the byte code uncomment the following lines
#import dis
#print(dis.dis(magic_calculation))
