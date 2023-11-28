#!/usr/bin/python3
def uppercase(str):
    for c in str:
        tmp = c
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(c) - 32)
        print("{}".format(tmp), end='')
        print()
