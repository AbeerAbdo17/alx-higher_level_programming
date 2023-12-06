#!/usr/bin/python3
def uniq_add(my_list=[]):
    un = set()
    for n in my_list:
        un.add(n)
    result = sum(un)
    return result
