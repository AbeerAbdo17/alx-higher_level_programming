#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
tmp = abs(number) % 10
if number < 0:
    tmp = -(tmp)
print("Last digit of {:d} is {:d} and is ".format(number, tmp), end = "")
if tmp > 5:
    print("greater than 5")
elif tmp == 0:
    print("0")
else:
    print("less than 6 and not 0")
