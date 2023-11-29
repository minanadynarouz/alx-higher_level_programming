def text_indentation(text):
    """ split a paragraphe into lines
    Args:
        text (str) -> Must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    idx = 0
    for i in range(len(text)):
        if i == len(text) - 1:
            print(text[idx:i + 1])
        elif text[i] in [".", "?", ":"]:
            print(text[idx:i + 1] + '\n')
            idx = i + 1
            while text[idx] == " ":
                idx += 1
