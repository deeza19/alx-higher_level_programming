#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    return len(a, b)

import marshal
fd = open("102-magic_calculation.py", "rb")
magic = fd.read(4) # python version specific magic num
date = fd.read(4) # compilation date
code_object = marshal.load(fd)
fd.close()
