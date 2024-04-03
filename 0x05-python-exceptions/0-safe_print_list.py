#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    
    try:
        my_list=[1, 4, 5]
        x = my_list[:3]
        print(x)

    except IndexError:
        print("Numbers are not up to 4")
