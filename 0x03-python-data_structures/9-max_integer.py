#!/usr/bin/python3
def max_integer(my_list=[]):
    max_n = my_list[0]
    for x in range(0, len(my_list)):
        if int(my_list[x] > int(max_n)):
            max_n = my_list[x]
    return max_n
