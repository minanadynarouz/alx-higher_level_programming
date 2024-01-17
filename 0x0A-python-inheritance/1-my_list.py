#!/usr/bin/python3
""" Class Mylist"""


class MyList(list):
    """Mylist class inherit from list"""

    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
