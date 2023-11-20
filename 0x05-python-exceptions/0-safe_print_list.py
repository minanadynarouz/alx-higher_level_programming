#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            pass
        else:
            counter += 1
    print()
    return (counter)
