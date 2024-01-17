#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list[:]
    index = 0
    while index < len(my_list):
        if search in newList:
            index = newList.index(search)
            newList[index] = replace
        index += 1
    return newList
