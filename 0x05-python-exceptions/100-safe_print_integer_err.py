#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except:
        error_message = "Exception: Unknown format code 'd' for object of type '{}'"
        print(error_message.format(type(value).__name__), file=sys.stderr)
        return False
