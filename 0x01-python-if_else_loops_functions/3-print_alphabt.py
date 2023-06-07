#!/usr/bin/python3
for ch_ascii in range(ord('a'), ord('z')+1):
    current = chr(ch_ascii)
    if current != 'e' and current != 'q':
        print("{}".format(current), end='')
