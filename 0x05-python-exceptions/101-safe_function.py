#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resu = fct(*args)
        return resu
    except Exception as xv:
        print("Exception:", xv, file=sys.stderr)
        return None
