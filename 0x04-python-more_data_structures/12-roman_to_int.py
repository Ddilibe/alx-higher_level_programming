#!/usr/bin/python3
def roman_to_int(roman_string):
    """Calculate the numeric value of a Roman numeral (in capital letters)"""
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [trans[r] for r in roman_string]
    return sum(
        val if val >= next_val else -val
        for val, next_val in zip(values[:-1], values[1:])
    ) + values[-1]
