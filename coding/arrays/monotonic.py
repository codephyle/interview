""" 
MONOTONIC ARRAY

Write a function that takes an array and returns a boolean representing whether the array is monotonic.

NOTE: Empty arrays and arrays of one element are monotonic

source: algoexpert.io
"""

def isMonotonic(a):

    if not a or len(a) == 1:
        return True

    inc = dec = False
    
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            inc = True
        else a[i] > a[i-1]:
            dec = True
    return inc or dec

isMonotonic( [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11])