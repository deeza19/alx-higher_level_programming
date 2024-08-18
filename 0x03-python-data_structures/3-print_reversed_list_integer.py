#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    for i in my_list:
        if i <= (len(my_list) - 1) and my_list != None: 
            i += 1
            reversed_num = my_list[-1-i]
            print("{:d}".format(int(reversed_num)))
        elif IndexError and True:
            return None
