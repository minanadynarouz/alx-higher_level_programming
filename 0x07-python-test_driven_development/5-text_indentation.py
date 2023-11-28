#!/usr/bin/python3

def text_indentation(text):
    """ split a paragraphe into lines
    Args:
        text (str) -> Must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i <= len(text) - 1:
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            i += 1
            print("\n")
        i += 1
