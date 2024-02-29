#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers using binary search
"""


def find_peak(list_of_integers):
    """Function to find a peak using binary search"""

    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]

    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
