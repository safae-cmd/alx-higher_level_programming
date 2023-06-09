#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_num = len(sys.argv) - 1
    if args_num == 1:
        print("{} argument:".format(args_num))
    else:
        print("{} arguments:".format(args_num))
    if args_num >= 1:
        for i, arg in enumerate(sys.argv[1:], start=0):
            if args_num != 0:
                print("{}: {}".format(i + 1, arg))
