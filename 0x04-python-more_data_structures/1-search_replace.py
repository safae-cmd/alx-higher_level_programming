#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(map(lamda a: replace if a == search else a, my_list))
    return new
