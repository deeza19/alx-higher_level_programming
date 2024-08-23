#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try: 
        for num in my_list[:x]:
            print(num, end="")
        print()
        return x
    except IndexError:
        print("Number of elements is not up to {:d}".format(x))
