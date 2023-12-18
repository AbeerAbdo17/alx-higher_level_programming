#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    xv = 0
    try:
        while xv is not x:
            print(my_list[xv], end='')
            xv = xv + 1
    except IndexError:
        None
    print()
    return xv
