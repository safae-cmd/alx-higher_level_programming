#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    sum_p = sum(a * b for a, b in my_list)
    sum_w = sum(b for a, b in my_list)
    return (sum_p / sum_w)
