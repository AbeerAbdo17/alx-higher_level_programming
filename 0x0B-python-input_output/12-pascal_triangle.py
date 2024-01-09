#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    """method scop"""
    if n <= 0:
        return []
    triang = [[1]]
    for i in range(1, n):
        xrow = [1]
        for j in range(1, i):
            xrow.append(triang[i - 1][j - 1] + triang[i - 1][j])
        xrow.append(1)
        triang.append(xrow)
    return triang
