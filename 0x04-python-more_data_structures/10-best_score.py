#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        bes = max(a_dictionary, key=a_dictionary.get)
        return bes
    else:
        return None
