#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: ", end="")
        return (result)
    except ZeroDivisionError:
        print("Inside result: {} ".format(None))
        return None
    finally:
        if b != 0:
            print("{}".format(a / b))
