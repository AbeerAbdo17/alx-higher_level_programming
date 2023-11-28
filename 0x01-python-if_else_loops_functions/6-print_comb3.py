#!/usr/bin/python3
for x in range(10):
    for j in range(x, 10):
        if x < j:
            print("{:2d}, {:2d}".format(x, j), end="\n" if x == 8 and j == 9 else ", ")
