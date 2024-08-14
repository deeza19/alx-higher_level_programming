#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97:
            result += str(ord(char) - 32)
            print("{}".format(result))
