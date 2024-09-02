#!/usr/bin/python3
"""A module that accesses and updates a private attribute square."""


class Square:
    """ A class that defines a square by a private instance attribute size with
    a property and a property setter."""

    def __init__(self, size=0):
        """A function that initialises the private instance attribute size."""
        self.size == size


    def size(self):
        """ Gets the size of the square and returns it
        """
        return self.__size


    def size(self, value):
        """A function that sets the private attribute size."""
        self.value = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """A function that returns the square area"""
        return self.__size ** 2
