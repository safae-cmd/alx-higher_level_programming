#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    return new.join([char for char in my_string if char.lower() != 'c' or char.upper() != 'C'])
