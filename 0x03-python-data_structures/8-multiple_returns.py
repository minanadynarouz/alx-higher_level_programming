#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] is not None:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
