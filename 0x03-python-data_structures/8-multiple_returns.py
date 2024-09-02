#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    elif sentence == "":
        return None, None
    else:
        sentence = len(sentence), sentence[0]
        return sentence
