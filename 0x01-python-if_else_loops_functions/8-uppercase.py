#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97:
            result += chr(ord(char) - 32)
            print("{}".format(result))
        else ord(char) >= 65 and ord(char) <= 90:
            print("{}".format(result))
