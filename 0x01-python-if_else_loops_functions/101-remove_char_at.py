#!/usr/bin/python3
def remove_char_at(str, n):
    nw = ''
    x = 0
    for c in str:
        if x != n:
            nw += str[x]
        x += 1
    return nw

