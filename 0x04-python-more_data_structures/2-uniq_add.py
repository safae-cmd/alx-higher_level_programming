#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()
    a = 0
    for i in my_list:
        if i not in unique_int:
            a += i
            unique_int.add(i)
    return (a)
