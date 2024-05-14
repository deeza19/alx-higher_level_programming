#!/usr/bin/python3
"""This is a module with class of square and SquareValidation
that raises an exception."""


class Square:
    """Created a class square with private instance attribute size."""
    def __init__(self, __size):
        self.__size = __size

class SquareValidation(Exception):
    """A user-defined exception class."""
    def __init__(self, size=0):
        Square.__init__(self, __size)
        Exception.__init__(self)
        self.size = size
    try:
        self.size = int(size)
        if size != int(size):
            raise SquareValidation(TypeError)
            print("size must be an Integer")
        if size < 0:
            raise SquareValidation(ValueError)
            print("size must be >= 0")
