#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for num in my_list:
        new_list = [num % 2 == 0]
        if num //2:
            return new_list
