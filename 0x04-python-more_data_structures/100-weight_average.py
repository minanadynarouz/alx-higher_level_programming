#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    mult = 0
    denominator = 0
    total = 0
    for x in my_list:
        mult += x[0] * x[1]
        denominator += x[1]
        total = mult/denominator
    return total
