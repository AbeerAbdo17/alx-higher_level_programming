#!/usr/bin/python3
""" comment for module"""


def add_integer(a, b=98):
    """
    add integer
    args:
    a and b must be int or float
    return:
    sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
