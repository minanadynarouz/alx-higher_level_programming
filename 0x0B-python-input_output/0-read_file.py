#!/usr/bin/python3

"""Read text from a file"""


def read_file(filename=""):
    """Function that read text file"""
    if filename:
        with open(filename, encoding="utf-8") as f:
            file = f.read()
            print(file, end="")
