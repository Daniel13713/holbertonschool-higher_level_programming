#!/usr/bin/python3
# Write a function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    """Find the maximum number"""
    arr = list_of_integers
    size = len(arr)
    value = None
    if size == 0:
        value = None
    elif size == 1:
        value = arr[0]
    else:
        for i in range(1, size - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                value = arr[i]
    return value


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
