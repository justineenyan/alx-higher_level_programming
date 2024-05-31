#!/usr/bin/python3
# Create a function def roman_to_int(roman_string):
# that converts a Roman numeral to an integer.
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    total = 0
    prev_value = 0

    for char in roman_string:
        # get the integer value for each character
        current_value = roman_to_int[char]
        # subtract 2 from the total + current value
        # and multiply by previous value
        if current_value > prev_value:
            total = total + current_value - 2 * prev_value
        else:
            total = total + current_value
            # update the values

            prev_value = current_value

    return total
