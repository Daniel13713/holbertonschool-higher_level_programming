#!/usr/bin/python3
# Write a function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    """Find the maximum number"""
    arr = list_of_integers
    size = len(arr)
    if size == 0:
        return None
    else:
        return max(arr)
