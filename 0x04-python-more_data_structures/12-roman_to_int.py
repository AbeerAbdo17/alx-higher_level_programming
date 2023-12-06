#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    nv = 0
    for xv in reversed(roman_string):
        nv = rom_num[xv]
        res += nv if res < nv * 5 else -nv
    return res
