#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    
    try:
        x = len(my_list)
        print(my_list)
        print(x)
    except IndexError.my_list:
        print("Numbers are not up to {:d}".format(x))
