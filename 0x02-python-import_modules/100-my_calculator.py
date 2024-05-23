#!/usr/bin/python3
import sys
from calculator_1 import add, subtract, multiply, divide
if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a1 = int(argv[0])
    operator = argv[1]
    b1 = int(argv[2])
    operators = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
            }

    if operator not in operators:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operation = operators[operator]
    result = operation(a1, b1)
    print("{:d} {:s} {:d} = {:d}".format(a1, operator, b1,result))
