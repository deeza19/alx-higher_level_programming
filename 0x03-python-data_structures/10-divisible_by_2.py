#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_2 = []
    for num in range(0, len(my_list)):
        if num % 2 == 0:
            mult_2.append(num)
        else:
            return None
    return mult_2
