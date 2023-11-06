#!/usr/bin/python3
def max_integer(my_list=[]):
    max = int(my_list[0])
    if not my_list:
        return None
    else:
        for int(i) in my_list:
            if i > max:
                max = i
    return max
