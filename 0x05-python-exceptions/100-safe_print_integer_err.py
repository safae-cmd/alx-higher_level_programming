#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except Exception as e:
        raise Exception("Exception:{}".format(e), file=sys.stderr)
        return False
