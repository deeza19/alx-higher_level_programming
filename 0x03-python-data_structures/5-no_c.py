#!/usr/bin/python3
def no_c(my_string):
    ascii_c = ord('c')
    ascii_C = ord('C')
    new_chars = []
    for char in my_string:
        if ord(char) not in (ascii_c, ascii_C):
            new_chars.append(char)
        new_string = ''.join(new_chars)
    return new_string
