#!/usr/bin/python3
"""This is a module.
It contains 2 classes, and 3 functions.
"""


class Square:
    """Created a square class with private instance attribute"""
    def __init__(self, __size):
        self.__size == __size

class SquareValidation(Exception):
    """A user-defined exception class"""
    def __init__(self, size=0):
        Square.__init__(self, __size)
        Exception.__init__(self)
        self.size = size
    
    try:
        size = int(size)
        if size not int:
            raise SquareValidation(TypeError)
            print("size must be an integer")
        if size < 0:
            raise bSquareValidation(ValueError)
            print("size must be >= 0")

def area(self):
    Square.__init__(self, __size)
    SquareValidation.__init__(self, size=0)
    items = self.size
    for item in items:
        return item**2

