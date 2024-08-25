#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for num in my_list:
            count += 1
            if isinstance(num, int):
                print("{:d}".format(num))
    except TypeError:
        return False
