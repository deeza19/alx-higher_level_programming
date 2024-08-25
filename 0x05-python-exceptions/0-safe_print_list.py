#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try: 
        count = 0
        for _ in my_list:
            count +=  1
        for num in my_list[:x]:
            if x > count:
                return count
            else:
                print(num, end="")
        print()
        return x
    except IndexError:
        print("Number of elements is not up to {:d}".format(x))
