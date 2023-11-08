#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if not roman_string or not isinstance(roman_string, str):
        return 0

    sum_of_num = 0
    prev_value = 0

    for char in roman_string:
        current_value = romans.get(char, 0)
        if current_value > prev_value:
            sum_of_num += current_value - 2 * prev_value
        else:
            sum_of_num += current_value

        prev_value = current_value

    return sum_of_num
