#!/usr/bin/python3

"""Write text to a file"""


def write_file(filename="", text=""):
    """ Append to the end of the file
    :param filename:
    :param text:
    :return: Count of written letters
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            oldData = f.tell()
            f.write(text)
            newData = f.tell()
            return newData - oldData
