#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list[idx] = element
    print("".format(my_list))
    if idx < 0:
        return my_list
        
