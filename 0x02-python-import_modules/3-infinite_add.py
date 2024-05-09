#!/usr/bin/python3
import sys


def add_arguments(*args):
    result = 0
    for arg in args:
        result += arg
    return result


if __name__ == "__main__":
    arguments = sys.argv[1:]
    arguments = [int(arg) for arg in arguments]
    result = add_arguments(*arguments)
    print(result)
