#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0

    sum_of_num = 0
    i = len(roman_string) - 1
    while i >= 0:
        num = romans[roman_string[i]]
        sum_of_num += num
        i -= 1
    return sum_of_num
