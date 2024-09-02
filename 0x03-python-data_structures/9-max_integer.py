#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        max = my_list[0]
        for number in my_list:
            if number > max:
                max = number
        return max
    elif my_list is empty or None:
        return None
