#!/usr/bin/python3
def magic_calculation(a, b):
    resu = 0
    for xv in range(1, 3):
        try:
            if xv > a:
                raise Exception('Too far')
            resu += a ** b / xv
        except Exception:
            resu = b + a
            break
    return resu
