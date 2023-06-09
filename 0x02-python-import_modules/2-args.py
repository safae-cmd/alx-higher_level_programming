#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    plural = "s" if args_num != 1 else ""
    
    print("Argument{}: {}".format(plural, args_num))
    
    if args_num > 0:
        print("Argument{}:".format(plural))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    elif args_num == 0
        print(".")
