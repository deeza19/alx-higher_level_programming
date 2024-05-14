#!/usr/bin/python3
"""This is a module with class of square that raises an exception
when validating the size of the square."""


class Square:
    """Created a class square with private instance attribute size."""
    def __init__(self, __size):
        self.__size = __size

    def __init__(self, size=0):
        self.__size = size
        if size != int(size):
            raise TypeError:
            print("size must be an Integer")
        if size < 0:
            raise ValueError:
            print("size must be >= 0")
