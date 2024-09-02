#!/usr/bin/python3
"""This is a module that defines a Sqaure class with 2 private instance
attribute and 2 public instance method."""


class Square:
    """A class that defines a square by private instance attributes and
    public instance methods"""

    def __init__(self, size=0, position=(0, 0)):
        """A function that initialises the private instance attribute size and
        A function that initialises the private instance position attribute
        of the square class"""
        self.size = __size
        self.position = __position


    def size(self):
        """A function that gets the size of the square"""
        return self.__size


    def size(self, value):
        """A function that sets the size of the square"""
        self.value = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def position(self):
        """a function that gets the position of the square"""
        return self.__position


    def position(self, value):
        """A function that sets the value of the position"""
        self.value = value
        if (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(i, int) and i > 0 for i in value)):
            self.__position = value
        else:
            raise ValueError("position must be a tuple of 2 positive integers")


    def area(self):
        """a function that returns the area of the square"""
        return self.size ** 2


    def my_print(self):
        """A function that prints in stdout with character #"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
