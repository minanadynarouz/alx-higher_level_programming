#!/usr/bin/python3
"""Insert line of text"""


def append_after(filename="", search_string="", new_string=""):
    """After string inert new_string
    Args:
        filename -> file to append to
        search_string -> string to search for and insert text after.
        new_string -> new text to be inserted after the found string.
    """
    lines = ""
    with open(filename, 'r+', encoding="utf-8") as f_r:
        for line in f_r:
            lines += line
            if search_string in line:
                lines += new_string

    with open(filename, 'w', encoding="utf-8") as f_w:
        f_w.write(lines)
