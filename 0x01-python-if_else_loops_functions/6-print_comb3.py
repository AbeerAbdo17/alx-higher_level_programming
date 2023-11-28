#!/usr/bin/python3
for x in range(10):
    for j in range(x + 1, 10):
        if x == 8 and j == 9:
            print("{}{}".format(x, j))
        else:
            print("{}{}".format(x, j), end=", ")
