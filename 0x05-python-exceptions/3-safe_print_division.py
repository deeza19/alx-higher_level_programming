#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        if True:
            print("Inside result: {:.1f}".format(result))
    except ZeroDivisionError:
        print("Inside result: None")
