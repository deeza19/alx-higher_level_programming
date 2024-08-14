#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try: 
        print(my_list[0:x-1], sep="")
    except IndexError:
        print("Number of elements is not up to {:d}".format(x))
