#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list:
        if my_list != None:
            print("{:d}".format(int(my_list[-1])))
            i -= 1
        else:
            return None
