#!/usr/bin/python3

"""Write text to a file"""


def write_file(filename="", text=""):
    """Write <text> to <filename> overriding
    Args:
        filename(str) -> Name of the file to write to
        text(str)     -> Content to write
    Returns:
        Number of characters written
    """
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            oldData = f.tell()
            f.write(text)
            newData = f.tell()
            return newData - oldData
