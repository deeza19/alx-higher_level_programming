#!/usr/bin/python3
import sys
def print_arguments():
    i = 1
    num_arguments = len(sys.argv) - 1
    if num_arguments < 1:
        print("{} arguments.".format(num_arguments))
    for i in range(1, len(sys.argv)):
        if num_arguments == 1:
            print("{} argument:".format(num_arguments))
            print("{:d}: {:s}".format(i, sys.argv[i]), sep="\n")
        elif num_arguments > 1:
            print("{} arguments:".format(num_arguments))
            print("{:d}: {:s}".format(i, sys.argv[i], sep="\n"))
if __name__ == "__main__":
    print_arguments()
