#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        for x in my_list:
            print("{:d}".format(x, sep=""))
        print(end="/n", x)
    except IndexError.my_list:
        print("Numbers are not up to {:d}".format(x))
