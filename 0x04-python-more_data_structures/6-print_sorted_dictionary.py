#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())
    for k in sort:
        print("{}: {}".format(k, a_dictionary[k]))
