#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = - number
    las = number % 10
    print("{}".format(las), end='')
    return las
