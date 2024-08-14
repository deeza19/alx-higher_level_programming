#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        print("{:d}".format(my_list[:x], sep=""))
        print("//n", )
    except TypeError:
        print("Numbers are not up to {:d}".format(x))
