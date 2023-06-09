#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_num = len(sys.argv) - 1
	if args_num == 0:
        print("{} arguments.".format(args_num))
    elif args_num == 1:
        print("{} argument:".format(args_num))
    else:
        print("{} arguments:".format(args_num))

    if args_num >= 1:
        i = 0
        for arg in sys.argv:
            if args_number != 0:
                print("{}: {}".format(i, arg))
            i += 1

