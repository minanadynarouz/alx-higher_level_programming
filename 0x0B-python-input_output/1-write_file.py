#!/usr/bin/python3

"""Write text to a file"""


def write_file(filename="", text=""):
    with open(filename, "w+", encoding="utf-8") as f:
        oldData = f.tell()
        f.write(text)
        newData = f.tell()
        return newData - oldData
