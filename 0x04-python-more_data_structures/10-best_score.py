#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    maxi = 0
    ke = ""
    for k, v in a_dictionary.items():
        if v > maxi:
            maxi = v
            ke = k
    return ke
