#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try: 
        return my_list[:x]
    except IndexError:
        print("Number of elements is not up to {:d}".format(x))
