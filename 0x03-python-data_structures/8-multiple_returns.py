#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        sentence[:1] = None
    else:
        sentence = len(sentence), sentence[0]
        return sentence
