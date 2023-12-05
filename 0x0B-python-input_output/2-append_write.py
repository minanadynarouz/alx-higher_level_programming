#!/usr/bin/python3

"""Write text to a file"""


def append_write(filename="", text=""):
    """Apend <text> to end of <filename>
    Args:
        filename(str) -> Name of the file to append to
        text(str)     -> Content to write
    Returns:
        Number of characters written
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            oldData = f.tell()
            f.write(text)
            newData = f.tell()
            return newData - oldData
