#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(0, len(str) - 1):
        if i != n:
            new_str[i] = str[i]
