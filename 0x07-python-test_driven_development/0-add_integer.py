#!/usr/bin/python3
"""This is a module."""


def add_integer(a, b=98):
    """A function that adds two integers"""
    if type(a, b) not in [int, float]:
        raise TypeError("a must be an integer") or ("b must be an integer")
    
    elif (a, b) in [float]:
        return int(a, b)
    return a + b
