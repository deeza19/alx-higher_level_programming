#!/usr/bin/python3
"""This is a module with class of square that raises an exception
when validating the size of the square."""


class Square:
    """A class square with private instance attribute size."""
    def __init__(self, __size):
        self.__size = __size
        """
        Constructs all the neccesary attributes for the size of the square."""

    def __init__(self, size=0):
        """
        Constructs all the neccessary attributes for the square object."""

        self.__size = size
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
