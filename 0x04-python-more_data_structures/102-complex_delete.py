#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newList = []
    for k, v in a_dictionary.items():
        if v == value:
            newList.append(k)

    for i in newList:
        a_dictionary.pop(i)
    return a_dictionary
