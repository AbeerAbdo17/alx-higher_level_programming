#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    bol = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as x:
        print("Exception:", x, file=sys.stderr)
        bol = False
    return bol
