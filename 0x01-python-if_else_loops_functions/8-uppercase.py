#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            upper_char = chr(ord(ch) - 32)
        else:
            upper_char = ch
        print("{}".format(upper_char), end='')
    print()
