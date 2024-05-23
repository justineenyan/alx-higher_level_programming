#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    new_result = add(a, b)
    print(f"{a} + {b} = {new_result}")

    new_result1 = subtract(a, b)
    print(f"{a} - {b} = {new_result1}")

    new_result2 = multiply(a, b)
    print(f"{a} * {b} = {new_result2}")

    new_result3 = divide(a, b)
    print(f"{a} / {b} = {new_result3}")
