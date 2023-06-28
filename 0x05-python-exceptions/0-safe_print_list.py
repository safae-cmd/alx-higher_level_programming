#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for _ in my_list:
            count += 1
        if x > count:
            x = count
        for i in range(x):
            print(my_list[i], end='')
        print()
        return x
    except TypeError:
        print("Something is wrong")
