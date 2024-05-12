#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    
    try:
        my_list=[1, 4, 5]
        for x in my_list[:x]:
            print(x, end="")
        print(end="\n")
            
    except IndexError.my_list:
        print("Numbers are not up to {:d}".format(x))
