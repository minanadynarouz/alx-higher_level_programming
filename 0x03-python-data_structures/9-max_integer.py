#!/usr/bin/python3
def max_integer(my_list=[]):
    maxNum = my_list[0]
    if not my_list:
        return None
    for i in my_list:
        if i > maxNum:
            maxNum = i
        else:
            pass
    return maxNum
