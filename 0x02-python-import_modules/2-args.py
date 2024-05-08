#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def print_arguments():
        num_arguments = len(argv) - 1
        if num_arguments == 1:
            print("{} argument:".format(num_arguments))
            print(sys.argv[1: ])
        elif num_arguments < 1:
            print("{} arguments.".format(num_arguments))
        elif num_arguments > 1:
            print("{} arguments:".format(num_arguments))
            print(sys.argv[1: ], sep="\n")
