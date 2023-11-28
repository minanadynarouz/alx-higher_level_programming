#!/usr/bin/python3

def print_square(size):
    """ Function to print squares of '#'
    Args:
        size(int/float) -> number of "#"'s to print
                        -> Must be an int or a float >= 0
    Returns nothing except if an exception occured
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
